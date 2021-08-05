import math

class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        while (True):
            if root*root<=x:
                return root
            root-=1

class Solution1:
    def mySqrt(self, x: int) -> int:
        return math.floor(x**(1/2))

class Solution2:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while (True):
            mid = (left+right) // 2
            if mid*mid>x: right = mid-1
            elif mid*mid<=x:
                if mid*mid==x or (mid+1)*(mid+1)>x: return mid
                else: left = mid+1
    
class Solution3:
    def mySqrt(self, x: int) -> int:
        return self.binSearchSqrt(x, 1, x)

    def binSearchSqrt(self, x:int, left: int, right: int):
        mid = (left+right) // 2
        if mid*mid>x: return self.binSearchSqrt(x, left, mid-1)
        elif mid*mid<=x:
            if mid*mid==x or (mid+1)*(mid+1)>x: return mid
            else: return self.binSearchSqrt(x, mid+1, right)





x = 4
print(Solution3().mySqrt(x))