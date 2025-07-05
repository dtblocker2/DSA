class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # the palindrome substring

        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome (single center)
            palindrome1 = expand_around_center(i, i)
            # Even-length palindrome (center between i and i+1)
            palindrome2 = expand_around_center(i, i+1)
            
            # Update longest palindrome found so far
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest

# Example usage
A = Solution()
print(A.longestPalindrome('babad'))  # Output could be "bab" or "aba"
