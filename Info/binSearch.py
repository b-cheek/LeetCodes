from typing import List

def binIter0(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if target<nums[m]: r = m-1
        elif target>nums[m]: l = m+1
        else: return m
    return -1

def binIter1(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)   #note that if this is the case, the difference is corrected for in line 18
    while l<r:
        m = (l+r)//2
        if target<nums[m]: r = m    #off by one difference corrected. Maybe faster because removing the -1 operation twice? less intuitive to me though
        elif target>nums[m]: l = m+1
        else: return m
    return -1

def binIter2(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if target<=nums[m]: r = m-1
        else: l = m+1
    return m    #the target must be in the list for this to work

def binRec0(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if target<nums[m]: r = m-1
        elif target>nums[m]: l = m+1
        else: return m
    return -1

def recHelper0

nums = [1, 2, 5, 7, 8, 10, 13, 14, 15, 19]

fn = binIter2
print(fn(nums, 1))
print(fn(nums, 2))
print(fn(nums, 5))
print(fn(nums, 7))
print(fn(nums, 8))
print(fn(nums, 10))
print(fn(nums, 13))
print(fn(nums, 14))
print(fn(nums, 15))
print(fn(nums, 19))
print(fn(nums, -1))
print(fn(nums, 20))