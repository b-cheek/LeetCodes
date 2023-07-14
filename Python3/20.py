# Valid Parentheses

from collections import deque

class Solution0:
    def isValid(self, s: str) -> bool:
        dq = deque()
        for char in s:
            if len(dq)==0: dq.append(char)
            elif char==')' and dq[-1]=='(': dq.pop()
            elif char==']' and dq[-1]=='[': dq.pop()
            elif char=='}' and dq[-1]=='{': dq.pop()
            else: dq.append(char)

        return len(dq)==0

class Solution1:
    def isValid(self, s: str) -> bool:
        reverseMap = {')':'(', ']':'[', '}':'{'}
        dq = deque()
        for char in s:
            if char not in reverseMap: 
                dq.append(char)
                continue
            elif len(dq) == 0 or reverseMap[char]!=dq[-1]: return False
            dq.pop()

        return len(dq)==0