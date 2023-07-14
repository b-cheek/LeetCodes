# Valid Anagram

class Solution0: #Why was this so slow? Perhaps consider checking length of inputs at start
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
            else:
                return False
        if t:
            return False
        return True

class Solution1: #Cheeky one liner but slow
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t)) #could have just done sorted(s) == sorted(t)

class Solution2: #idk why this is slow, but it is good on space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        wordsArr = [0]*26
        for i in s:
            wordsArr[ord(i)-ord('a')] += 1
        
        for i in t:
            index = ord(i) - ord('a')
            wordsArr[index] -= 1
            if wordsArr[index] < 0: return False   
            
        return True
            
class Solution3: #Like S2 but with a hash map, making it faster
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        wordsDict = {}
        
        for i in range (0, len(s)):
            wordsDict[s[i]] = wordsDict.get(s[i], 0) + 1
            wordsDict[t[i]] = wordsDict.get(t[i], 0) - 1
            
        for key in wordsDict:
            if wordsDict[key]: return False
            
        return True

class Solution4: #Like S3, but create separate dicts for each string. Somehow slow?
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        wordsDict1 = {}
        wordsDict2 = {}
        
        for i in range (0, len(s)):
            wordsDict1[s[i]] = wordsDict1.get(s[i], 0) + 1
            wordsDict2[t[i]] = wordsDict2.get(t[i], 0) + 1
            
        return wordsDict1 == wordsDict2
            