class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #equiavlent of trim in python
        if s==" ":
            return 1
        max_length = 0
        for i in range(len(s)):
            substring = s[i:]
            unique_characters = []
            for j in range(len(substring)):
                #find a ways to add element to set or tuple and know if there is duplicate entry
                # print(substring,max_length)
                if substring[j] in unique_characters:
                    # print(substring,max_length)
                    length_of_substring = len(unique_characters)
                    break
                unique_characters.append(substring[j])
                if j == len(substring)-1:
                    length_of_substring = len(unique_characters)
            max_length = max(max_length, length_of_substring)

        return max_length

A = Solution()

# print(A.lengthOfLongestSubstring('abcabcbb'))
print(A.lengthOfLongestSubstring('au'))
# print(A.lengthOfLongestSubstring('pwwkew'))

''' Above code is piece of shit as it is of O(n^3)'''

