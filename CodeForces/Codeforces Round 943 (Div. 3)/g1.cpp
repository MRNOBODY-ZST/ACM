#include <bits/stdc++.h>
using namespace std;
vector<int> Zfunc(string &str)
{
    int n = str.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++)
    {
        if (i <= r)
        {
            z[i] = min(r - i + 1, z[i - l]);
        }
        while (i + z[i] < n && str[z[i]] == str[i + z[i]])
        {
            z[i]++;
        }
        if (i + z[i] - 1 > r)
        {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}
int f(vector<int> &z, int len)
{
    int n = z.size();
    int cnt = 1;
    for (int i = len; i < n;)
    {
        if (z[i] >= len)
        {
            cnt++;
            i += len;
        }
        else
        {
            i++;
        }
    }
    return cnt;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        string s;
        cin >> n >> k >> k >> s;
        vector<int> z = Zfunc(s);
        int l = 0, r = n + 1;
        while (r - l > 1)
        {
            int mid = (l + r) / 2;
            if (f(z, mid) >= k)
            {
                l = mid;
            }
            else
            {
                r = mid;
            }
        }
        cout << l << "\n";
    }
}