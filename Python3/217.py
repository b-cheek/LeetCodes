# Contains Duplicate

from typing import List

class Solution0:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)): 
            if nums[i] in nums[0:i]: return True
        return False

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = []
        for i in nums:
            if i in numsDict: return True
            numsDict.append(i)
        return False

class Solution2: ## Note that sets use hashing for access, that's why it's good
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in nums:
            if i in numsSet: return True
            numsSet.add(i)
        return False

class Solution3: ## Cheeky one liner, takes advantage of sets having no duplicates. Not as good as S2
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)>len(set(nums))
        
s = Solution1()
nums=[0, 1, 3, 3, 0]
print(s.containsDuplicate(nums))