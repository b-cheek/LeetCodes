# Neetcode vid: https://www.youtube.com/watch?v=jzZsG8n2R9A
# This problem is clearly an extension of 2 sum, but it's a little different
# because there are duplicate values in the input, and we need to submit every valid triplet (without a duplicate triplet)
# Sorting makes it easy to ignore duplicates, since they will be adjacent.
# Since we are already sorting, we can then use the two pointer 2sum strategy also used in P1.1 and P167
class Solution: # O(nlogn + n(n+1)/2) -> O(n^2) time (nlogn from sort, but O(n(n+1)/2) for following because 2 sum only iterates on nums after i, see triangular number
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # Stop at positive integers, since a valid solution must include a negative value
            if num > 0:
                break

            # If num has already been visited, skip it (duplicate value, thus == previous num, need to check bounds as well)
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointer 2sum implementation
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    # The next lines are improvements we can make based on 3sum structure
                    l += 1  # Both l and r changed because num stays same so changing neither or one has to be a duplicate or invalid triplet
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # l pointer (chosen arbitrarily) moved until no longer a duplicate
                        l += 1
                        
        return res
