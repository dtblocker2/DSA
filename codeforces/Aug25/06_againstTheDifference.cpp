#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;
    while (T--) {
        int n;
        cin >> n;
        vector<int> a(n + 1);
        for (int i = 1; i <= n; ++i) cin >> a[i];

        vector<vector<int>> pos(n + 1);
        vector<int> occ(n + 1, 0);
        vector<int> dp(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            int v = a[i];
            occ[v]++;            
            dp[i] = dp[i - 1];     

            if (occ[v] >= v) {
                int left;
                if (v == 1) {
                    left = i;
                } else {
                    left = pos[v][occ[v] - v];
                }
                dp[i] = max(dp[i], dp[left - 1] + v);
            }

            pos[v].push_back(i);
        }

        cout << dp[n] << '\n';
    }
    return 0;
}