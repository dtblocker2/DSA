#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, output = 0;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        int maxN = a[0];
        for (int i = 0; i < n; i++) {
            if (a[i] > maxN) {
                maxN = a[i];
            }
            if ((i % 2 == 1) && (a[i] < maxN)) {
                a[i] = maxN;
            }
        }

        for (int i = 0; i < n; i++) {
            if (i == 0 && n > 1) {
                while (a[1] <= a[0] && a[0] > 0) {
                    output += a[0] - a[1] + 1;
                    a[0] = a[1] - 1;
                }
                /* if ( a[0] >= a[1]) {
                    a[0] = a[1] - 1;
                    output += a[0] - a[1] + 1;
                }; */
            }

            if ((i % 2 == 0) && (i != 0) && (i != n - 1)) {
                while (a[i+1] <= a[i] && a[i] > 0) {
                    output += a[i] - a[i+1] + 1;
                    a[i] = a[i+1] - 1;
                }
               /* if ( a[i] >= a[i+1]) {
                    a[i] = a[i+1] - 1;
                    output += a[i] - a[i+1] + 1;
                }; */
                while (a[i-1] <= a[i] && a[i] > 0) {
                    output += a[i] - a[i-1] + 1;
                    a[i] = a[i-1] - 1;
                }
               /* if ( a[i] >= a[i-1]) {
                    a[i] = a[i-1] - 1;
                    output += a[i] - a[i-1] + 1;
                }; */
            }

            if (i == n - 1 && (n - 1) % 2 == 0 && n != 1) {
                while (a[n-2] <= a[n-1] && a[n-1] > 0) {
                    output += a[n-1] - a[n-2] + 1;
                    a[n-1] = a[n-2] - 1;
                }
               /* if ( a[0] >= a[1]) {
                    a[0] = a[1] - 1;
                    output += a[0] - a[1] + 1;
                }; */
            }
        }

        cout << output << endl;
    }

    return 0;
}
