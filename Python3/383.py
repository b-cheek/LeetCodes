# Ransom Note

# Naive solution, remove each letter in ransome note from magazine, and if magazine doesn't have that letter return false
# Note that the list conversion is necessary, the string replace() method doesn't do anything if the search string isn't present
class Solution0: # O(n + n^2) -> O(n^2)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            try: magazine.remove(letter)
            except: return False

        return True


# Dictionary solution, store letters in a dictionary as keys, value is the numebr of occurrences
# Subtract ocurrences in ransomNote, if there isn't a value to match return false
class Solution1: # O(n + n) -> O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        for letter in magazine:
            magazineDict[letter] = magazineDict.get(letter, 0) + 1

        for letter in ransomNote:
            if letter not in magazineDict or magazineDict[letter]==0: return False
            magazineDict[letter]-=1

        return True


# Same as above, but using list instead of dict (hash function is ord(letter)-ord('a'), guarantees no collisions)
class Solution2: 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = [0]*26
        for letter in magazine:
            magazineDict[ord(letter) - ord('a')] += 1

        for letter in ransomNote:
            if magazineDict[ord(letter) - ord('a')] == 0: return False
            magazineDict[ord(letter) - ord('a')] -= 1

        return True


# Using python's Counter object, subtract all the letters in magazine from counter,
# if there is anything left then it must not have been present in magazine.
from collections import Counter

class Solution3: # O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)