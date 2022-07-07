def veryNaiveStringMatch(haystack, needle): #returns index of needle in haystack, -1 if otherwise
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle: return i
    return -1

def naiveStringMatch(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        match = True
        for j in range(len(needle)):
            if haystack[i+j]!=needle[j]: 
                match = False
                break
        if match: return i
    return -1

# Code from https://youtu.be/JoF0Z7nVSrA
# Also helpful https://youtu.be/V5-7GzOfADQ
# I PREFER THE SIMPLE IMPLEMENTATION BELOW
def kmpStringMatch(haystack, needle):
    if needle == "": return 0
    #Note that getting the lps[] is most complicated, but to reduce big O of whole alg, this must also be faster than O(mn)
    def getLPS(s): #"LPS" is longest prefix suffix 
        lps = [0] * len(s) #lps[n] = LPS of s[0:n]
        prevLPS = 0 #this variable is hard to understand because it is used as a value and an index, see video
        i = 1 #lps[1] always = 0 P/S cannot equal whole word

        #This for loop moves window of where to find LPS
        while i<len(s): #can't use for loop, because i doesn't always increment
            if s[i] == s[prevLPS]: #in the case where the last char of window matches the end of new possible P
                lps[i] = prevLPS + 1 #Since prevLPS was a match and the new end char matches, LPS for s[0:i] = LPS of prev P + 1
                prevLPS += 1 #updates prevLPS as val, and increments the size of a possible P when prevLPS is index
                i += 1 #move end of checking range
            
            #This section is if the current char does not match the end of the P
            elif prevLPS == 0: #no P matched S in prev string, prevLPS pointer at beginning of needle
                lps[i] == 0 #therefore P can't match S here, since there are either 2 letters, or i did not advance in the last step (prevLPS only decreases in the else statement below)
                i+=1 #only advance i
            else: #before the prevLPS pointer has reached needle[0]
                prevLPS = lps[prevLPS-1] #moving prevLPS back to check for a shorter matching suffix
        return lps

    lps = getLPS(needle)
    j = 0 #ptr for haystack
    i = 0 #ptr for needle

    while i < len(haystack):
        if haystack[i] == needle[j]: # If matching, carry on checking each
            i += 1 
            j += 1
        else: #if not matching
            if j==0: i += 1 #if at beginning of needle
            else: j = lps[j-1] #needle goes to where last match could be because of prefix suffix matching
        if j==len(needle): #If you reach end of pattern, there is a match
            return i - len(needle) #returns index where needle begins (index would be +1, but i was incremented in first if)
    return -1

#code from https://leetcode.com/problems/subtree-of-another-tree/discuss/474425/JavaPython-2-solutions%3A-Naive-Serialize-in-Preorder-then-KMP-O(M%2BN)-Clean-and-Concise
def kmpStringMatchSimple(haystack, needle):
    def getLPS(needle):
            m = len(needle)
            j = 0
            lps = [0] * m
            for i in range(1, m): #lps[1] must be 0, P/S < len(s)
                while needle[i] != needle[j] and j > 0: j = lps[j-1] #shorten P length until match or beginning of needle
                if needle[i] == needle[j]: #in case j==0
                    j += 1 #move end of prefix to right, aka increase prefix length by 1
                    lps[i] = j #set longest prefix of s[0:i]
            return lps
        
    lps = getLPS(needle)
    n, m = len(haystack), len(needle)
    j = 0
    for i in range(n):
        while haystack[i] != needle[j] and j > 0: j = lps[j-1]
        if haystack[i] == needle[j]: #if matching, check next letter pair
            j += 1
            if j == m: return i-len(needle)+1 #if you've reached the end, return index where needle begins
    return -1

print(veryNaiveStringMatch("search", "arch"))
print(naiveStringMatch("search", "arch"))
print(kmpStringMatch("search", "arch"))
print(kmpStringMatchSimple("search", "arch"))

print(kmpStringMatch("aabaaabaaac", "aabaaac"))
print(kmpStringMatchSimple("aabaaabaaac", "aabaaac"))