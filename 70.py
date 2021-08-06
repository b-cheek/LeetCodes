from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution0:
    def climbStairs(self, n: int) -> int:
        return self.recClimb(n, [1, 1])[0]

    def recClimb(self, n: int, d: List) -> tuple:
        if n==1: return [1, d]
        elif n-2>=len(d):
            d.append(self.recClimb(n-2, d)[0])
            d.append(self.recClimb(n-1, d)[0])
        elif n-1>=len(d):
            d.append(self.recClimb(n-1, d)[0])
        return (d[n-1] + d[n-2], d)

class Solution1: 
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        tempMinus2 = 1
        tempMinus1 = 2
        while (n>3):
            tempMinus2, tempMinus1 = tempMinus1, tempMinus1+tempMinus2
            n-=1
        return tempMinus1+tempMinus2

            
        
# print(Solution1().climbStairs(4))
# print(Solution0().climbStairs(4))

for i in range(1, 46):
    print(str(i) + ": " + str(Solution0().climbStairs(i)) + " " + str(Solution1().climbStairs(i)))