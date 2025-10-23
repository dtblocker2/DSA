#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n, k;
        std::string s;
        std::cin >> n >> k >> s;

        int output = 0;
        int z = -k;

        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                if (i - z >= k) {
                    output++;
                    z = i;
                } else {
                    z = i;
                }
            }
        }

        std::cout << output << std::endl;
    }

    return 0;
}
