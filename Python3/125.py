class Solution0: ## Functions
    def isPalindrome(self, s: str) -> bool:
        flatStr = ''.join(filter(lambda char : char.isalnum(), s)).lower()
        return flatStr == flatStr[::-1]

class Solution1: # Two pointer, O(n)
    def isPalindrome(self, s: str) -> bool:
        slower = s.lower() # Funny
        front = 0
        back = len(s)-1

        while front <= back:
            if not slower[front].isalnum(): ## Should have just done while loops
                front += 1                  ## but I wanted to be fancy
                continue
            if not slower[back].isalnum():
                back -= 1
                continue

            if slower[front] != slower[back]: return False
            
            front += 1
            back -= 1

        return True