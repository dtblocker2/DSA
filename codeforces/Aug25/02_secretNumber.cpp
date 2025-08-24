#include <list>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    list<list<long long unsigned int>> outputArr;

    for (int p = 0; p < t; p++) {
        long long int unsigned n;
        cin >> n;

        int x = 1;
        long long int unsigned temp = 11;
        list<long long unsigned int> output;

        long long unsigned int z = pow(10,18);
        if (n!=z)
        {
            for (int q=0; q<18; q++) {
                if (n % temp == 0) {
                    // cout<<temp<<endl;
                    output.push_front(n / temp);
                }
                x++;
                temp = pow(10, x) + 1;
            }
        };

        outputArr.push_back(output);
    }

    for (auto testCase : outputArr)
    {
        if (testCase.empty())
        {
            cout<<0;
        }
        else
        {
            cout<<testCase.size()<<endl;
        };

        for (auto val : testCase)
        {
            cout << val<< " ";
        }
        cout<<endl;
    }

    return 0;
}

// faster answer

/* 
Great — you’re basically coding the solution to **“The Secret Number”** problem 👍.
Your current code works but can be **cleaned up and optimized**. Let me point out improvements:

---

## 🔹 Issues in your current code

1. **Unnecessary use of `list<list<...>>`**
   → `vector<vector<...>>` is simpler, faster, and more natural here.

2. **`pow(10, x)` returns double**
   → dangerous for big integers (`10^18` might be inaccurate). Better to build powers of 10 using integer multiplication.

3. **Special case `n == 10^18`**
   → you check it manually with `if (n!=z)`, but you don’t need this; just loop safely up to `18`.

4. **Push from front (`push_front`)**
   → not necessary, order can be controlled by sorting at the end.

5. **Extra loop (`for (q=0; q<18`)**
   → you can just loop `k` from 1 to 18 and stop when denominator > n.

---

## 🔹 Improved Version

Here’s a **cleaner, faster, and safer** solution:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        unsigned long long n;
        cin >> n;

        vector<unsigned long long> results;

        unsigned long long p10 = 10; // 10^1
        for (int k = 1; k <= 18; k++) {
            unsigned long long denom = p10 + 1; // 10^k + 1
            if (denom > n) break;              // no need to continue
            if (n % denom == 0) {
                results.push_back(n / denom);
            }
            if (k < 18) p10 *= 10; // prepare next power of 10
        }

        if (results.empty()) {
            cout << 0 << "\n";
        } else {
            sort(results.begin(), results.end());
            cout << results.size() << "\n";
            for (size_t i = 0; i < results.size(); i++) {
                if (i) cout << " ";
                cout << results[i];
            }
            cout << "\n";
        }
    }

    return 0;
}
```

---

## 🔹 Why this is better

* ✅ Uses `vector` instead of `list` (simpler & cache-friendly).
* ✅ No floating-point `pow()`, only integer multiplication.
* ✅ No need for `if (n!=10^18)` special case.
* ✅ Proper formatting of output with spaces.
* ✅ Sorted ascending as required by the problem.

---

⚡ Complexity:

* At most 18 checks per test case → O(18·t) = O(t), which is very efficient.

---

Would you like me to also **explain step-by-step with an example** (say `n=1111`) how this code finds `x=11` and `x=101`?

*/
