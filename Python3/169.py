class Solution0:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if i in hashMap.keys():
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            if hashMap[i]>len(nums)/2: return i