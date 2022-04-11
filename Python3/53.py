from typing import List

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

class Solution1: 
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

class Solution2: #basically a more complicated version of solution 3
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
        

c = Solution2()
nums = [-1]
print(c.maxSubArray(nums))