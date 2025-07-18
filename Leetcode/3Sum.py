""" My answer First thought no optimisation with O(N^3) time complexity this is complete piece of shit though logic is correct what will you do of logic if it can't give answer fast"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []
        if n<3:
            return 'write nums greater than 3 elements'
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    # print(i,j,k)
                    if (nums[i]+nums[j]+nums[k])==0:
                        m = [nums[i],nums[j],nums[k]]
                        m.sort()
                        if m not in output:
                            output.append(m)

        
        return output.sort()

A = Solution()

""" print(A.threeSum([-1,0,1,2,-1,-4]))
print(A.threeSum([0,1,1]))
print(A.threeSum([0,0,0])) """
# print(A.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))

""" g = [[-3, 1, 2], [-2, 0, 2], [-4, 2, 2], [-3, -2, 5], [-5, 0, 5], [-10, 5, 5]]
g.sort()
print(g) """

""" 
You're absolutely right in your self-reflection — your **O(N³)** solution works logically but is **computationally expensive**, especially for large inputs. Let's improve it together.

### ❌ Problems in Your Code:
1. **Inefficient Triple Loop:** Brute forcing all 3-combinations gives **O(N³)** time — not scalable.
2. **Redundant Sorting + Membership Check (`if m not in output`)** — costly **O(N)** inside O(N³), making it even worse.
3. ✅ `sort()` returns `None`, so `return output.sort()` gives **`None`** instead of the list. You probably meant:
   ```python
   output.sort()
   return output
   ```

### ✅ Optimal Solution (O(N²)) — Using Sorting + Two Pointers:

The optimal solution uses:
- **Sorting** → O(N log N)
- **Iterating + Two Pointers** → O(N²)

### 🔧 Fixed Code (Efficient Version):

```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the list
        n = len(nums)
        output = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    # Move both pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return output
```

### ✅ Test Cases:

```python
A = Solution()
print(A.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(A.threeSum([0, 1, 1]))              # []
print(A.threeSum([0, 0, 0]))              # [[0, 0, 0]]
print(A.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
```

### 📈 Time Complexity:
- Sorting: **O(N log N)**
- Two-pointer search: **O(N²)** in worst case

Much better than **O(N³)**!

### 🧠 TLDR:
- 🧮 Brute-force is fine for tiny input, but inefficient for real-world scales.
- ✅ Always prefer O(N²) solutions with sorting + two-pointers for 3-sum problems.
- 🚫 `output.sort()` returns `None`, don’t return it directly.

If you'd like, I can help you visualize this using an example step-by-step!

 """