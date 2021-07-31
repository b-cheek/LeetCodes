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
        
        return mid


s = Solution()
nums = [0, 2, 3, 4, 5, 6, 7]
tar = 3
print (s.searchInsert(nums, tar))