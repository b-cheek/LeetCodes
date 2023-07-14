# Maximum Subarray

from typing import List
from math import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        max = -float('inf')
        for i in range(0, len(nums)):
            if nums[i]>0:
                for j in range(i+1, len(nums)+1):
                    if j>0:
                        subArrSum = 0
                        for num in nums[i:j]:
                            subArrSum+=num
                        if subArrSum>max:
                            max = subArrSum
                        print(nums[i:j], subArrSum)
        if max>float('inf'): return max
        for i in nums:
            if i>max:
                max = i
        return max
                            
class Solution0:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)>2:
            return self.maxSubArray([self.maxSubArray(nums[:len(nums)//2]), self.maxSubArray(nums[len(nums)//2:])])
        elif len(nums)==2:
            return max(nums[0], nums[1], nums[0]+nums[1])
        else: return nums[0]

class Solution1: #Basicallyyyyy Kadane's algorithm 
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        max = -float('inf')
        for i in range(0, len(nums)):
            if nums[i]>0:
                subArrSum = 0
                for j in nums[i:]:
                    subArrSum+=j
                    print(subArrSum)

        if max>float('inf'): return max
        for i in nums:
            if i>max:
                max = i
        return max

class Solution2: #basically a more complicated version of solution 1!?
    def maxSubArray(self, nums: List[int]) -> int:
        pointer = 0
        subArrTotal = 0
        max = -float('inf')
        allNegativeMax = max
        while pointer<len(nums):
            subArrTotal+=nums[pointer]
            if nums[pointer]>allNegativeMax: allNegativeMax = nums[pointer]
            if subArrTotal<=0: subArrTotal = 0
            if subArrTotal>max: max = subArrTotal
            pointer+=1
        if allNegativeMax<0: return allNegativeMax
        return max

## DP version of Kadane's alg I think
class Solution3: #dp, create array of the sum of previous sumarrays, but when it goes below 0 start back at 0 because that's >=
    def maxSubArray(self, nums: List[int]) -> int:
        numsLen = len(nums)
        dp = [0]*numsLen
        maxNum = dp[0] = nums[0]

        if numsLen>1:
            for i in range(1, numsLen):
                dp[i] = nums[i] + (0 if dp[i-1]<=0 else dp[i-1])
                maxNum = max(maxNum, dp[i])

            return maxNum

        else:
            return nums[0]
        
class Solution4: ## Readable version of Kadane's alg. O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = -inf ## You could do nums[0], but -inf is more readable imo, and works for len=0 even though not necessary
        for num in nums:
            curSum = max(curSum+num, num)
            maxSum = max(maxSum, curSum)

        return maxSum

class Solution5: ## Recursive DP (memoization). Kind of like Kadane's with preprocessing? See 121.4
    def maxSubArray(self, nums: List[int]) -> int:
        @cache ## Memoizes solve() so it doesn't have to recalculate every time
        def solve(stop: int) -> int:
            if stop==0: return nums[0]
            return max(solve(stop-1)+nums[stop], nums[stop])

        ## I don't like that I have to do this, but the alternative is wack and the memoization works the same
        return max(solve(i) for i in range(len(nums)))

class Solution6: ## Tabulation is strangely similar to S5. Is it strange or am I dumb?
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        dp[0] = res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i-1], 0) ## Note that bringing nums[i] out of the max is shorter, but conveys the idea less clearly
            res = max(res, dp[i])

        return res

class Solution7: ## Memoization like in S5, but without using @cache
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [nums[0]] + ["empty"]*(len(nums)-1) ## I don't like mixing types here but see the comment below this Solution
        def solve(stop: int) -> int:
            if memo[stop] is not "empty": return memo[stop]
            memo[stop] = max(solve(stop-1)+nums[stop], nums[stop]) ## I went back to the S5 way
            return memo[stop]

        return max(solve(i) for i in range(len(nums)))

## This solution has especially made me realize that tabulation is just the right way to do this.
## The problem I had with this is how to represent if a subproblem solution had been memoized.
## Originally used a dictionary, but I wanted to use array to reflect how each entry corresponds to a stop index.
## But now I had to check if an entry existed in a new way.
## In theory any integer could be used, so I had to mix types, and decided a string "empty" would be best.
## I thought about adding items to the list as they are memoized and checking size, or using a sentinel value.
## However, this very clearly shows why tabulation is correct because you kind of just end up generating the list in a tabular way.
## In retrospect, I shouldn't have done the memoization solutions, but hey learning experience

## This solution uses divide and conquer. The subproblems are
##   * The max subarray in the left half
##   * The max subarray in the right half
##   * The max subarray that crosses the midpoint
class Solution8: ## Divide and conquer. O(nlogn) from recurrence relation T(N) = 2T(N/2) + O(N) using master theorem
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left: int, right: int) -> int:
            if left==right: return nums[left] ## Base case
            mid = (left+right)//2
            leftMax = solve(left, mid) ## Max subarray in left half
            rightMax = solve(mid+1, right) ## Max subarray in right half

            ## Max subarray that crosses the midpoint
            ## This is computed by finding the largest subarrays adjacent to the midpoint, where one (arbitrarilly chosen to be left) includes the midpoint
            ## which when combined  will yield the largest subarray that includes the midpoint
            leftSum = -inf
            rightSum = -inf
            curSum = 0

            for i in range(mid, left-1, -1): ## Largest subarray adjacent to left and including midpoint (this is why the for loop must iterate backwards)
                curSum+=nums[i]
                leftSum = max(leftSum, curSum)
            curSum = 0 ## Reset curSum for right side
            for i in range(mid+1, right+1): ## Largest subarray adjacent to right
                curSum+=nums[i]
                rightSum = max(rightSum, curSum)

            return max(leftMax, rightMax, leftSum+rightSum)
            ## Note that I originally had mid separate ^ because leftSum + rightSum doesn't totally imply that it includes the mid.
            ## However, doing it like this is necessary for edge cases of small arrays (very important at lowest level of recursion lol)
            ## and I'm tired, so sorry for bad readability :( hope it's not too confusing

        return solve(0, len(nums)-1)

## To optimize S8, we can skip the step of finding the max subarray including nums[mid] with some preprocessing.
## We'll use DP (tabulation) to compute pre[i] = max subarray ending at nums[i] and suf[i] = max subarray starting at nums[i].
## Then, the max subarray that crosses the midpoint is just pre[mid]+suf[mid+1] (note that the left side includes mid again).
class Solution9: ## Divide and conquer with preprocessing. O(n) from recurrence relation T(N) = 2T(N/2) + O(1) using master theorem
    def maxSubArray(self, nums: List[int]) -> int:                                                    ## ^ From preprocessing
        pre = [0]*len(nums)
        suf = [0]*len(nums)
        pre[0] = nums[0] ## Base case
        suf[-1] = nums[-1] ## Base case
        ## To elaborate on base case, pre and suf are built bottom up with tabulation.
        ## The bottom of pre is pre[0] same as dp in S6. Suf is build in the opposite way, so it's "bottom" is the last element.

        for i in range(1, len(nums)):
            pre[i] = max(pre[i-1]+nums[i], nums[i]) ## Create pre in the same way as dp in S6(note I put nums[i] back in the max for readability)
            suf[-i-1] = max(suf[-i]+nums[-i-1], nums[-i-1]) ## This is doing the same thing backwards. I would make a different for, but this is better
                                                            ## And the for condition is weirder so equally hard to read.

        def solve(left: int, right: int) -> int:
            if left==right: return nums[left]

            mid = (left+right)//2
            leftMax = solve(left, mid)
            rightMax = solve(mid+1, right)
            crossMax = pre[mid]+suf[mid+1]

            return max(leftMax, rightMax, crossMax)

        return solve(0, len(nums)-1)

## But wait! If we're calculating pre and suf in the same way we calculated dp[] in s6, why not just use that
## with the much simpler implementation. So yeah. Just use DP. Hell, use Kadane's algorith. How did I end up here?

c = Solution4()
nums = [-1]
print(c.maxSubArray(nums))