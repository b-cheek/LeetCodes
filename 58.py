import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArr = s.strip().split(" ")
        return len(strArr[-1])
        
class Solution0:
    def lengthOfLastWord(self, s: str) -> int:
        lastWords = re.findall('\w+', s)
        print(lastWords)
        if len(lastWords)>0: return len(lastWords[-1])
        return 0

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordLen = 0
        for i in range(-1, -len(s)-1, -1):
            if s[i]!=" ":
                for j in range(i, -len(s)-1, -1):
                    print(j)
                    if s[j]!=" ": lastWordLen+=1
                    if (j==-len(s) or s[j]==" "): return lastWordLen
        return lastWordLen


        
c = Solution1()
s = "day"
print(c.lengthOfLastWord(s))