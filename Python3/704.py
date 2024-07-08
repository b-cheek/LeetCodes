# Binary Search

class Solution0: #iterative
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r: ## Yes, <= is necessary
            m = (l+r)//2 ## Rewrite as m = l+(r-l)//2 to avoid overflow. Not necessary here, but LOOK AT CONSTRAINTS!
            if target<nums[m]:
                r = m-1
            elif target>nums[m]:
                l = m+1
            else:
                return m
        return -1

class Solution1:    #recursive
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(self, nums: List[int], l: int, r: int) -> int:
            if l>r: return -1
            m = (l+r)//2
            if target<nums[m]:
                return binSearch(self, nums, l, m-1)
            elif target>nums[m]:
                return binSearch(self, nums, m+1, r)
            return m
        
        return binSearch(self, nums, 0, len(nums)-1)

class Solution2: # Built in
    def search(self, nums: List[int], target: int) -> int:
        return i if nums[i:=(bisect.bisect(nums, target)-1)] == target else -1