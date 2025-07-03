class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_instance = None
        for i in range(len(word)):
            if word[i] == ch:
                first_instance = i
                break
        if first_instance is None:
            return word
            
        output = word[first_instance+1:]
        print(output,first_instance)
        
        for i in range(first_instance+1):
            output = word[i] + output
        
        return output

A = Solution()

print(A.reversePrefix("abcdefd",'d'))

print(A.reversePrefix("rzwuktxcjfpamlonbgyieqdvhs",'s'))