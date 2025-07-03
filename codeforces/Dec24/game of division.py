def can_win(n, k, a):
    # Try each possible index i
    for i in range(n):
        is_winning = True
        # Check against all other indices j
        for j in range(n):
            if i != j:
                # If we find any j where |ai - aj| is divisible by k,
                # then i is not a winning choice
                if abs(a[i] - a[j]) % k == 0:
                    is_winning = False
                    break
        # If we found no j where |ai - aj| is divisible by k,
        # then i is a winning choice
        if is_winning:
            return i + 1  # Convert to 1-based indexing
    return -1  # No winning choice found

# Read number of test cases
t = int(input())
output = []
for _ in range(t):
    # Read n and k
    n, k = map(int, input().split())
    # Read array a
    a = list(map(int, input().split()))
    
    # Find winning index
    result = can_win(n, k, a)
    
    if result == -1:
        output.append("NO")
    else:
        output.append("YES")
        output.append(result)

for z in output:
    print(z)