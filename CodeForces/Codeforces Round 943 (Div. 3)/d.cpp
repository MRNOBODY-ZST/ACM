#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using ui = unsigned int;
using us = unsigned short;

const ll N = 3e5 + 5;
ll a1, a2, c, i, k, m, m1, m2, n, pb, ps, s, t, u;
ll a[N], b[N];
bitset<N> v = 0;

void dfs(ll i, ll &m)
{
    m = max(m, a[i]);
    v[i] = 1;
    if (!v[b[i]])
        dfs(b[i], m);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> t;
    while (t)
    {
        cin >> n >> k >> pb >> ps;
        for (i = 1; i <= n; ++i)
            cin >> b[i];
        for (i = 1; i <= n; ++i)
            cin >> a[i];
        m1 = m2 = 0;
        for (i = 1; i <= n; ++i)
            v[i] = 0;
        dfs(pb, m1);
        for (i = 1; i <= n; ++i)
            v[i] = 0;
        dfs(ps, m2);
        a1 = a[pb] * k;
        u = pb;
        c = s = 0;
        for (;;)
        {
            s += a[u];
            ++c;
            if (a[u] == m1)
                break;
            u = b[u];
            if (c <= k)
                a1 = max(a1, s + a[u] * (k - c));
        }
        a2 = a[ps] * k;
        u = ps;
        c = s = 0;
        for (;;)
        {
            s += a[u];
            ++c;
            if (a[u] == m2)
                break;
            u = b[u];
            if (c <= k)
                a2 = max(a2, s + a[u] * (k - c));
        }
        cout << (a1 < a2 ? "Sasha\n" : a1 > a2 ? "Bodya\n"
                                               : "Draw\n");
        --t;
    }
    return 0;
}