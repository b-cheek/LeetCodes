# Problem is basically fibonacci

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

# Improved for readability
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n<=3: return # There are n unique ways to climb n steps when n<=3, ([1]=1, [1,1]=[2]=2, [1,1,1]=[2,1]=[1,2]=3)
        # The main recursive relation for the dp is that climbStairs(n) = climbStairs(n-1) + climbStairs(n-2):
        two_steps_before = 2 # Value represents the number of unique ways to climb n-2 steps
        one_step_before = 3 # Same but with n-1 steps
        for _ in range (n-3): # Since our base case covered the first 3 values for climbStairs(n), 
                              #we just need to iterate n-3 more times to get to n
            res = one_step_before+two_steps_before # Recurrence relation
            # Move to next iteration, shift steps back by one
            two_steps_before = one_step_before
            one_step_before = res
            # Note that the reasoning for having the iteration be after calculation is a good exercise for the reader
            # in balancing efficiency, readability, and concision

        return res
            
        
# print(Solution1().climbStairs(4))
# print(Solution0().climbStairs(4))

for i in range(1, 46):
    print(str(i) + ": " + str(Solution0().climbStairs(i)) + " " + str(Solution1().climbStairs(i)))