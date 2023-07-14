# Range Sum Query - Immutable

class NumArray0:

    def __init__(self, nums: List[int]):
        self.accu = [0]
        for i in nums:
            self.accu += self.accu[-1] + i

    def sumRange(self, left: int, right: int) -> int: 
        return self.accu[right+1] - self.accu[left]


class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range (left, right+1):
            sum += self.nums[i]

        return sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)