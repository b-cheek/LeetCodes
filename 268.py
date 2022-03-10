from typing import List

class Solution0:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range (0, len(nums)): 
            if i != nums[i]: return i
        return len(nums)

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(0, len(nums)):
            res ^= i
            res ^= nums[i]
        return res


s = Solution1()
nums = [1, 0, 2, 3]
print(s.missingNumber(nums))