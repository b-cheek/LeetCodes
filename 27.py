from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0: return 0
        i = 0
        while i<len(nums):
            if nums[i]==val: 
                nums.pop(i)
            else: i+=1
        return len(nums)

class Solution0:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size==0: return 0
        i = 0
        for j in range (0, size-1):
            if nums[j]!=val: 
                nums[i] = nums[j]
                i+=1
        return i

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size==0: return 0
        i = 0
        while i<size:
            if nums[i]==val:
                nums[i] = nums[size-1]
                size-=1
            else: i+=1
        return i

nums = [3]
val = 2
s = Solution()
print (s.removeElement(nums, val))
