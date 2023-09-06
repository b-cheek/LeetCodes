# Search in Rotated Sorted Array

from typing import List

# Use binary search to find the pivot (the unshifted start of the array, AKA smallest element)
# Then use binary search in both sorted halves to find the target
# Example:
#          ⬐ pivot
# [4,5,6,7,0,1,2]
#  \     / \   /
# sorted portions
#          
class Solution0:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l + r) // 2
            if nums[m] > nums[-1]: # If pivot is right of m
                l = m + 1
            else: # Pivot is m, or left of m
                r = m - 1
            # You may be thinking that if pivot is m, this would eliminate m from the search space
            # This is correct, but recall that when the search ends, l>r.
            # I'm not going to spend too long trying to understand or explain this.

        def binSearch(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1

        # If target is in the left sorted portion, return its index
        if (answer := binSearch(0, l-1, target)) != -1: # Note walrus operator :=
            return answer

        # Otherwise return its index in the right sorted portion
        return binSearch(l, len(nums)-1, target)
        
        # Make above a one liner with falsey coalescence! Not quite as readable
        # return (binSearch(0, l-1, target)+1 or binSearch(l, len(nums)-1, target)+1) - 1
        # For more info, see elvis operator, short circuit or, nullish coalescence

# Instead of searching both halves, just search the rotated array
# shifting by the pivot amount whenever you read the array
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Bin search (BS) to find pivot, is L value at end of BS
        pivot, r = 0, n - 1

        while pivot<=r:
            m = (pivot + r) // 2
            if nums[m] > nums[-1]:
                pivot = m + 1
            else:
                r = m - 1

        # Mostly a typical BS...
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            # ...except we shift by the pivot when reading from nums
            if nums[(m+pivot) % n] < target:
                l = m + 1
            elif nums[(m+pivot) % n] > target:
                r = m - 1
            else:
                return (m+pivot) % n

        return -1


# This solution eliminates the need for two separate binary searches
# by determining a sorted half of the list each iteration.
# Looking at our example:
# [4,5,6,7,0,1,2]
# At each index, you can see that one half is sorted, and other half is unsorted.
# Using this information, we can check if the target is in the sorted half, and if
# not then it must be in the unsorted half. This still cuts the search size in half
# each iteration, leading to our one pass O(logn) solution
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # If the left half is sorted
            elif nums[m] > nums[l]: # This can also be >=, and still works; Doing it this way just covers the = in the else case
                # If target is within the left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: # It must be in the right half
                    l = m + 1

            else: # The right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


# This solution cuts down the search in a similar way to S2;
# however it does so by finding where the pivot is in relation to m and the target.
# Note that you can remove the repeated l = m + 1, r = m - 1 lines
# by using more complex control flow, or a new variable, but
# I find this way to be the most readable
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # If m and target are on the same side of the pivot (See explanation at top for clarification):
            if (nums[m] < nums[0]) == (target < nums[0]):
                # Perform normal binary search logic
                if nums[m] < target: l = m + 1
                elif nums[m] > target: r = m - 1
                else: return m

            # Otherwise, m and target are on opposite sides of the pivot.
            # Since m and target are on opposite sides, we reduce the search area by
            # setting the search area to go from m, in the direction of target.
            
            # If m is left of the pivot, target is to it's right
            elif nums[m] > nums[0]:
                l = m + 1

            # m is right of the pivot, target is to it's left
            else:
                r = m - 1    

        return -1
        

s = Solution2()
lists = [
    [[4,5,6,7,0,1,2], 0],
    [[5,6,7,0,1,2,4], 0],
    [[6,7,0,1,2,4,5], 0],
    [[7,0,1,2,4,5,6], 0],
    [[0,1,2,4,5,6,7], 0],
    [[0], 0],
    [[0], 1],
    [[0,1], 0]
]

for l in lists:
    print(s.search(l[0], l[1]))