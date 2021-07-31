from typing import List

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (high+low) // 2
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1
            
            else: return mid
        
        return low

class Solution0:

    def binSearch(self, val, nums, left, right):
        if left>right: 
            return left

        mid = (left+right) // 2

        if val==nums[mid]:
            return mid
        
        elif val > nums[mid]:
            return self.binSearch(val, nums, mid+1, right)

        else:
            return self.binSearch(val, nums, left, mid-1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]: 
            return 0
        elif target>nums[-1]: 
            return len(nums)
        return self.binSearch(target, nums, 0, len(nums)-1)

class Solution1: #this is a slow solution, the guy in the comments was capping

    def binSearch(self, val, nums, left, right):
        if left<=right:

            mid = (left+right) // 2

            if val==nums[mid]:
                return mid

            elif val > nums[mid]:
                if val<nums[mid+1]:
                    return mid+1

                else:
                    return self.binSearch(val, nums, mid+1, right)

            else:
                return self.binSearch(val, nums, left, mid-1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]: 
            return 0
        elif target>nums[-1]: 
            return len(nums)
        return self.binSearch(target, nums, 0, len(nums)-1)
    

s = Solution0()
nums = [1, 3, 5]
tar = 4
print (s.searchInsert(nums, tar))