#include <bits/stdc++.h>
using namespace std;
bool cmp2(pair<int, int> a, pair<int, int> b)
{
    return a.second < b.second;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    pair<int, int> a[n];
    for (int i = 0; i < n; i++)
    {
        a[i].first = i;
        cin >> a[i].second;
    }
    sort(a, a + n, cmp2);
    int m = 0x3f3f3f;
    for (int i = 0; i < n - k; i++)
    {
        int ma = 0;
        int mi = 0x3f3f3f;
        for (int j = i; j < i + k; j++)
        {
            ma = max(ma, a[j].first);
            mi = min(mi, a[j].first);
        }
        m = min(ma - mi, m);
    }
    cout << m << '\n';
    return 0;
}
