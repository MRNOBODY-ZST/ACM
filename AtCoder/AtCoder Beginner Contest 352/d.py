# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# i = [0 for _ in range(n)]
# tmp = 2e5 + 5
# for r in range(n):
#     i[p[r] - 1] = r
# for r in range(n - k):
#     template = i[r + k - 1] - i[r]
#     if template > 0:
#         tmp = min(tmp, template)
# print(tmp)
#convert the code below to Python
# #include <bits/stdc++.h>
# using namespace std;
# bool cmp2(pair<int, int> a, pair<int, int> b)
# {
#     return a.second < b.second;
# }
# int main()
# {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#     int n, k;
#     cin >> n >> k;
#     pair<int, int> a[n];
#     for (int i = 0; i < n; i++)
#     {
#         a[i].first = i;
#         cin >> a[i].second;
#     }
#     sort(a, a + n, cmp2);
#     int m = 0x3f3f3f;
#     for (int i = 0; i < n - k; i++)
#     {
#         int ma = 0;
#         int mi = 0x3f3f3f;
#         for (int j = i; j < i + k; j++)
#         {
#             ma = max(ma, a[j].first);
#             mi = min(mi, a[j].first);
#         }
#         m = min(ma - mi, m);
#     }
#     cout << m << '\n';
#     return 0;
# }
n, k = map(int, input().split())
a = 
a.sort(key=lambda x: x[1])
m = 0x3f3f3f
for i in range(n - k):
    ma = 0
    mi = 0x3f3f3f
    for j in range(i, i + k):
        ma = max(ma, a[j][0])
        mi = min(mi, a[j][0])
    m = min(ma - mi, m)
print(m)
