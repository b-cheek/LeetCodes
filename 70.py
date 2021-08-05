from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution0:
    def climbStairs(self, n: int) -> int:
        return self.recClimb(n, {})

    def recClimb(self, n: int, d: dict) -> tuple:
        if n==0 or n==1: 
            d[n] = 1
            return [1, d]
        else:
            if (n-1) in d:
                if (n-2) in d:
                    d[n] = d[n-1] + d[n-2]
                else:
                    climb = self.recClimb(n-2, d)
                    d = climb[1]
                    d[n] = d[n-1] + climb[0]
                return [d[n], d]
            else:
                if (n-2) in d:
                    climb = self.recClimb(n-1, d)
                    d = climb[1]
                    d[n] = climb[0] + d[n-2]
                else:
                    d[n] = self.recClimb(n-1, d) + self.recClimb(n-2, d)
                return 
        

for i in range(0, 10):
    print(str(i) + ": " + str(Solution0().climbStairs(i)))