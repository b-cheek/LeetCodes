class Solution0: #See Solution 2 for a better version of this
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typeWord(s: str) -> str:
            wordDQ = deque([])
            for char in s:
                if char=="#":
                    if len(wordDQ)>0:
                        wordDQ.pop()
                else: wordDQ.append(char)
            
            res = ""
            while wordDQ:
                res += wordDQ.popleft()

            return res
                
        return typeWord(s)==typeWord(t)
        
class Solution1: #In place going forwards, took me too long and not the best though
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typeWord(s: str) -> str:
            wordPointer=0
            while wordPointer<len(s):
                if s[wordPointer]=="#":
                    if wordPointer==0: #If we're at the front of the word
                        s = s[1:]
                        wordPointer -= 1 #Because we're only removing the #
                    else:
                        s = s[:wordPointer-1] + s[wordPointer+1:]
                        wordPointer -= 2 #because we're deleting a # and the char it backspaces
                wordPointer += 1
            return s
                
        return typeWord(s)==typeWord(t)

class Solution2: #Adapted from LC solution
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            ans = deque([])
            for c in s:
                if c != '#':
                    ans.append(c)
                elif ans: #Important check here
                    ans.pop()
            return "".join(ans) #I didn't know you could do this
        return build(s) == build(t)

class Solution3: #Adapted from https://leetcode.com/problems/backspace-string-compare/discuss/1995817/Daily-LeetCoding-Challenge-May-Day-1/1371825
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            ans = ""
            backspace = 0
            
            for i in range(len(s)-1, -1, -1): #Working backwards is better because you don't have to realize you delete a char after iterating ovver it
                if s[i] == "#":
                    backspace += 1
                else:
                    if backspace == 0: #This is what I couldn't think of when I was trying to write this 
                        ans += s[i]
                    else:
                        backspace -= 1
                        
            return ans
        
        return build(s) == build(t)
        
class Solution4: #adapted from previous solution, but now in place!
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            backspace = 0
            curBackspaceTotal = 0 #This is used to check if we are in the middle of a "backspaced segment," either during the for loop or after
            
            firstChar = 0
            while s[firstChar]=="#": firstChar += 1
            s = s[firstChar:] #We trim all #s from the front of the string since they don't do anything
            
            for i in range(len(s)-1, -1, -1):
                if s[i] == "#":
                    backspace += 1
                    curBackspaceTotal += 1
                elif curBackspaceTotal>0: #If we are in a "backspaced segment"
                    if backspace == 0:
                        s = s[:i+1] + s[i+2*curBackspaceTotal+1:] #if we hit zero, then we have iterated over an equal # of backspaces and characters, so we need to delete 2*curBackspaceTotal chars in front of i
                        curBackspaceTotal = 0
                    else:
                        backspace -= 1
                        
            if curBackspaceTotal>0: #If we end the loop in the middle of a backspaced segment
                s = s[2*curBackspaceTotal-backspace:] #better though of as curBackspaceTotal + (curBackspaceTotal - backspace), since we must account #s (curBackspaceTotal) and chars yet to be backspaced (in parentheses)

            return s

        return build(s) == build(t)
        