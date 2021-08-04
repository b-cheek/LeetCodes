from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num+=str(i)
        num = int(num) + 1
        numArr = []
        for i in str(num):
            numArr.append(i)
        return numArr

class Solution0:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1:
            if digits[0]==9:
                return [1,0]
            digits[0]+=1
            return digits
        if digits[-1]==9:
            digits = self.plusOne(digits[0:-1])
            digits.append(0)
            return digits
        digits[-1]+=1
        return digits

class Solution1: #bad solution
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1:
            if digits[0]==9:
                return [1,0]
            return [digits[0]+1]
        if digits[-1]==9:
            digits = self.plusOne(digits[0:-1])
            digits.append(0)
            return digits
        digits[-1]+=1
        return digits

s = Solution1()
digits = [9]
print(s.plusOne(digits))
