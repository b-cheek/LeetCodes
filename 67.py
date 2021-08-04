from typing import List

class Solution:
    def addBinary(self, a: str, b: str, carry="0") -> str:
        if len(b)>len(a): a, b = b, a
        a = list(a)
        b = list(b)
        print(a, b)
        for i in range (1, len(b)+1):
            if a[-i] == b[-i]:
                carry = a[-i] + carry
                a[-i] = "0"
            else: 
                carry = "0" + carry
                a[-i] = "1"
        for i in carry:
            if i=="1":
                return self.addBinary(carry, a)
        if a[0] == "0": return "".join(a[1:])
        return "".join(a)


s = Solution()
a = "100110"
b = "111111"
print(s.addBinary(a, b))

