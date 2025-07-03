#Brute force solution

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        lenght_of_substring=1
        output=0

        while lenght_of_substring<= len(s):
            for j in range(len(s)-lenght_of_substring+1):
                substring=""
                for i in range(lenght_of_substring):
                    substring += s[j+i]
                if (substring[0]==c) and (substring[-1]==c):
                    output+=1
                    #print(substring)

            lenght_of_substring+=1

        #print(output)
        return output
    

#optimized

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return count * (count + 1) // 2
