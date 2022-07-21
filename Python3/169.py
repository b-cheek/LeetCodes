class Solution0: #Skipped a brute force solution
    def majorityElement(self, nums: List[int]) -> int: #O(n)
        hashMap = {}
        for i in nums: #1 comparison + 2 operations at least n times
            if i in hashMap.keys(): 
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            if hashMap[i]>len(nums)/2: return i

class Solution1: #Simpler control flow, idk why faster
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums: #1 comparison + 2/3 operations at least n times
            if i not in hashMap.keys():
                hashMap[i] = 0
            hashMap[i] += 1
            if hashMap[i]>len(nums)/2: return i

class Solution2: #From LC solution
    def majorityElement(self, nums: List[int]) -> int: #O(n)
        import collections
        counts = collections.Counter(nums) #? operations n times
        return max(counts.keys(), key=counts.get) #2 operations n times?

class Solution3: #From LC Solution
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #O(nlgn)
        return nums[len(nums)//2] #This works because we are finding a MAJORITY element, not a plurality

class Solution4: #Using randomness is actually an interesting and sensible approach considering that one element has >50% chance at being chosen at random
    def majorityElement(self, nums: List[int]) -> int:
        import random
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

class Solution5: #Divide and conquer, valuable demo but not fast
    def majorityElement(self, nums, lo=0, hi=None) -> int:
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo #Since the full array is being passed each time, we are choosing the index range to evaluate a majority element
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)

class Solution6: #This is genius, look at it on the LC page 🤤
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate