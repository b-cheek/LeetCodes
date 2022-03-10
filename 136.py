from typing import List

class Solution0: #sorting
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if i+1>=len(nums) or nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i+=2

class Solution1: #bit manip XOR
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            xor^=num

        return xor

            

s = Solution1()
l = [1, 2, 2, 3, 1]
print(s.singleNumber(l))
        