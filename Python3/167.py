class Solution0: # Two pointer, O(n) time O(1) aux. space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while (numbers[l] + numbers[r] != target): # Probably should have generalized this to work if there is not a solution
            if numbers[l] + numbers[r] < target: l += 1
            else: r -= 1

        return [l+1, r+1]