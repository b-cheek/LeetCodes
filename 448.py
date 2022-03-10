from typing import List

class Solution0: #this is bad
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                for j in range (nums[i-1]+1, nums[i]): res.append(j)
        if not (len(nums) in nums): res.append(len(nums))
        return res

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingNums = [True] * len(nums)
        for i in nums: missingNums[i-1] = False
        res = []
        for i in range (0, len(missingNums)):
            if missingNums[i]: res.append(i+1)
        return res

class Solution2: #worse lol
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range (1, len(nums)+1): 
            if i not in nums: res.append(i)
        return res

class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if nums[abs(i)-1]>0: nums[abs(i)-1]*=-1

        print(nums)
        res = []
        for i in range (0, len(nums)): 
            if nums[i]>0: res.append(i+1)

        return res


s = Solution3()
nums = [1, 1, 1]
print(s.findDisappearedNumbers(nums))


