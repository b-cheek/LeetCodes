# Two Sum

class Solution0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceDict = {target-nums[0]: 0}
        for i in range (1, len(nums)):
            if nums[i] in differenceDict:
                return [differenceDict[nums[i]], i]
            else:
                differenceDict[target-nums[i]] = i
            

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()  # Sort arr in increasing order by their values.
        
        left, right = 0, len(arr) - 1
        while left < right:
            sum2 = arr[left][0] + arr[right][0]
            if sum2 == target:
                return [arr[left][1], arr[right][1]]
            elif sum2 > target:
                right -= 1  # Try to decrease sum2
            else:
                left += 1  # Try to increase sum2

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceDict = {}
        for i in range (len(nums)):
            if nums[i] in differenceDict:
                return [differenceDict[nums[i]], i]
            differenceDict[target-nums[i]] = i

class Solution3: #Using enumerate for the for loop
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for numID, num in enumerate(nums):
            if num in numsDict: return [numsDict[num], numID]
            numsDict[target-num] = numID