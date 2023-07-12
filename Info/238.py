class Solution0:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # O(3n) time, O(3n) space (including output array)
        # Preprocess array product_from_start[i] = product of all nums up to (not including) i
        product_from_start = [1] * len(nums) # The 1 is just a placeholder, except for the first iteration of the loop as a base case
        for i in range(1, len(nums)): # Fill the remainder of the array, product_from_start[0] is already 1
            product_from_start[i] = product_from_start[i-1] * nums[i-1] # Equal to the last value multiplied by the next num in nums

        # Same deal in reverse
        product_from_end = [1] * len(nums)
        for i in range (len(nums)-2, -1, -1): # Range looks weird, but remember start is inclusive, end is exclusive
            product_from_end[i] = product_from_end[i+1] * nums[i+1]

        for i in range(len(nums)): # Populate result array with product of all numbers left and right
            nums[i] = product_from_start[i] * product_from_end[i]

        return nums

# Optimize S0 by using the result array as the product_from_start array, and using a variable to store the product from the end,
# which is possible since we only need the last used value of product_from_end
class Solution1: # O(2n) time, O(n) space (including output array)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)): 
            res[i] = res[i-1] * nums[i-1]

        cur_product_from_end = 1 # Base case like before

        for i in range(len(nums)-2, -1, -1):
            res[i] *= nums[i+1] * cur_product_from_end
            cur_product_from_end *= nums[i+1] # Update cur_product_from_end for next iteration

        return res


# Optimize S1 by just using the variable technique for both directions, allowing us to calculate res in 1 pass.
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # O(n) time, O(n) space (including output array)
        res = [1] * len(nums)
        prefix_product = suffix_product = 1

        for i in range(len(nums)): # i and -1-i start at each end of list, and move to opposite end
            res[i] *= prefix_product
            res[-i-1] *= suffix_product
            prefix_product *= nums[i]
            suffix_product *= nums[-1-i]

        return res