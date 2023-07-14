# Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        if needleLength == 0: return 0
        for i in range (0, len(haystack)-needleLength+1):
            print(i, haystack[i:i+needleLength])
            if haystack[i:i+needleLength] == needle: return i
        return -1

s = Solution()
string = "abchelloabc"
find = "hello"
print(s.strStr(string, find))