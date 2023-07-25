# Permutations

# This solution generates each permutation by picking each number in nums and adding it to the current permutation,
# as long as it is not already in the current permutation. This happens recursively, so that each permutation is created
class Solution0:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(cur, length):
            if length == len(nums): 
                res.append(cur.copy())
                return
            for num in nums:
                if num not in cur:
                    helper(cur.copy() + [num], length + 1) # I think doing copy here is what makes this slow.
                                                           # Since inorder DFS, this is technically unnecessary

        for num in nums: # I realize now that I could have just done helper([], 0) like S3 instead of this loop
            helper([num], 1)
        
        return res


# This solution recursively generates permutations by rotating parts of the list
# (Rotating is shifting elements over, where the elements at the end flow back to the front;
# for example, [1,2,3] -> [2,3,1])
# The idea is that you get all rotations of nums;
# Then with each rotation, you get all rotations only rotating elements 1 through the end of the list
# You continue this recursively to get all permutations
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [nums] # Start with the unrotated list, you'll see why later
        n = len(nums)

        def rotations(i, cur): # The problem with this solution is that passing in cur.copy() is memory intensive
            # Get all the rotations not including the original list (this is why we start with the original list in res)
            # If we looped from i->n to include the original list, the recursion would not work since the unrotated original list
            # will be the same as unrotated elements 1 through the end in the first iteration of the for loop of the first recursive call
            for j in range(i+1, n):
                # Get the rotation by slicing the list
                newList = cur[0:i] + cur[j:] + cur[i:j] # and getting slices like this is slow
                res.append(newList)
                # Get all permutations of the rest of the elements
                rotations(i+1, newList)

            if i<n: rotations(i+1, cur.copy()) # Get permutations of the unmodified list

        rotations(0, nums)
        return res


# This solution is like the last solution, but improves in a few ways.
# Mainly, it implements backtracking by using pop and append to rotate the list instead of slicing.
# This is the neetcode solution, so check out his video
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1: # Base case, only permutation is the list itself
            return [nums.copy()]

        # This is like S1 in that it sets 1 element, then gets permutations of the rest.
        # This algorithm sets elements at the end though using pop(0) and append
        for _ in range(len(nums)): # Get all rotations, a rotation is done by popping the first element and appending it to the end
            n = nums.pop(0)
            perms = self.permute(nums) # Get all permutations of the rest of the elements
            for perm in perms:
                perm.append(n) # Add the popped element to the end of each permutation

            res.extend(perms) # Add all permutations to the result
            nums.append(n) # Put the popped element back in the list to complete rotation
        
        return res


# This solution is like S0 but with backtracking, doesn't use fancy rotation to remove the need to check for duplicates like S1 and S2
# I guess since rotating is O(n), and checking for duplicates is O(n) it all works out
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur):
            # If you have a full permutation, add it to the result
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            # Otherwise, add a number not yet in the permutation and recurse
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
                    # You don't need a copy of cur! you can use the same instance, since you add and pop for each child.
                    # Here is a brief demonstration with permutations of [1,2,3,4] (each node represents what cur looks like):
                    #           [1]
                    #       /    |    \
                    #     [1,2] [1,3] [1,4]
                    # This is just a small part of what the whole tree would look like, but having this visual makes it more clear how
                    # cur goes from [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]; you can see that cur is the same instance throughout

        backtrack([])
        return res

        # Here is an example of what cur would look like at each step of the recursion on [1,2,3]
        # [] -> [1] -> [1,2] -> [1,2,3] -> [1,3] -> [1,3,2] -> [1,2] -> [1] -> [2] -> [2,1] -> [2,1,3] -> [2,3] -> [2,3,1] -> [2,1] -> [2] -> [3] -> [3,1] -> [3,1,2] -> [3,2] -> [3,2,1] -> [3,1] -> [3] -> []

# See Heap's algorithm and Steinhaus-Johnson-Trotter algorithm for more efficient algorithms