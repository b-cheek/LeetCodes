# Counting Bits

import math
from typing import List

class Solution0:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range (0,n+1):
            ones = 0
            temp = i

            while temp>0:
                temp-=2**math.floor(math.log2(temp))
                ones += 1

            res.append(ones)
        
        return res

class Solution1:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        pow2 = 1
        for i in range(1, n+1):
            if i==pow2*2:
                res.append(1)
                pow2 *= 2
            else:
                res.append(1 + res[i-pow2])

        return res

class Solution2:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            res.append(res[i>>1] + i%2)

        return res
            

s = Solution1()
n=10
print(s.countBits(n))

