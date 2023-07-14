# Remove Duplicates from Sorted Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == (0 or 1): return size
        i = 0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i+=1
        return (len(nums))

class Solution0:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == (0 or 1): return size
        i = 0
        for j in range (1, size-1):
            if (nums[j] != nums[i]):
                i+=1
                nums[i] = nums[j]
        return i+1

s = Solution0()
nums = [0,0,1,1,1,2,2,3,3,4]
print (s.removeDuplicates(nums))
