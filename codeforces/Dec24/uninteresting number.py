def is_divisible_by_9(t, test_cases):
    results = []
    
    for n in test_cases:
        # Calculate the sum of the digits of the number
        digit_sum = sum(int(digit) for digit in n)
        
        # Check if the current sum is already divisible by 9
        if digit_sum % 9 == 0:
            results.append("YES")
            continue
        
        # Check if replacing any digit x with x^2 can make the sum divisible by 9
        found = False
        for i, digit in enumerate(n):
            original_digit = int(digit)
            # Only consider digits 0, 1, 2, 3 as their squares are single digits
            if original_digit in [0, 1, 2, 3]:
                squared_digit = original_digit ** 2
                new_sum = digit_sum - original_digit + squared_digit
                if new_sum % 9 == 0:
                    found = True
                    results.append("YES")
                    break
        
        # If no replacement works, output "NO"
        if not found:
            results.append("NO")
    
    return results


# Input reading and output
t = int(input())  # Number of test cases
test_cases = [input().strip() for _ in range(t)]

# Process and print results
results = is_divisible_by_9(t, test_cases)
print("\n".join(results))