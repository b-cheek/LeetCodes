class Solution0: #Store sorted strings as keys in dict, value is list of corresponding anagrams 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in anagramDict:
                anagramDict[sortedString].append(string)
            else: anagramDict[sortedString] = [string]
        res = []
        for key in anagramDict:
            res.append(anagramDict[key])
        return res

class Solution1: #Use an array representation string (see 242.2) as key instead
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for string in strs:
            stringProfile = [0]*26
            for char in string:
                stringProfile[ord(char)-ord('a')] += 1
            stringProfile = str(stringProfile) # Note that I could use tuple as well, since alse immutable
            if stringProfile in anagramDict:
                anagramDict[stringProfile].append(string)
            else: anagramDict[stringProfile] = [string]
        res = []
        for key in anagramDict:
            res.append(anagramDict[key])
        return res

class Solution2: #Use defaultdict to handle creation of keys
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())