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
    return m    #the target must be in the list for this to work, but it is faster

def binRec0(nums: List[int], target: int) -> int:
    # return recHelper0(nums, target, 0, len(nums)-1)
    # return recHelper1(nums, target, 0, len(nums)-1)
    # return recHelper2(nums, target, 0)
    numsDict = {'not found': -1}
    for i in range(0, len(nums)):
        numsDict[nums[i]] = i
    return numsDict[recHelper3(nums, target)]

def recHelper0(nums: List[int], target: int, l: int, r: int):
    if l>r: return -1
    m = (l+r)//2
    if target<nums[m]: return recHelper0(nums, target, l, m-1)
    if target>nums[m]: return recHelper0(nums, target, m+1, r) 
    return m #note that you don't need else because of the return statement

def recHelper1(nums: List[int], target: int, l: int, r: int): #This function does NOT WORK, meant to illustrate that checking for equality makes the recursive version significantly simpler
    if l>r: return m
    m = (l+r)//2    #note that I considered passing m each time to solve the issue of m not being declared, but then I want to calculate m in the recursive statement
    if l>r: return m+1
    if target<=nums[m]: return recHelper1(nums, target, l, m-1)
    return recHelper0(nums, target, m+1, r) #note that you don't need else because of the return statement

def recHelper2(nums: List[int], target: int, diff: int):
    if len(nums)==0: return -1
    m = (len(nums)-1)//2
    if target<nums[m]: return recHelper2(nums[0:m], target, diff)
    if target>nums[m]: return recHelper2(nums[m+1:], target, diff+m+1)
    return diff+m

def recHelper3(nums: List[int], target: int):
    if len(nums)==0: return 'not found'
    m = (len(nums)-1)//2
    if target<nums[m]: return recHelper3(nums[0:m], target)
    if target>nums[m]: return recHelper3(nums[m+1:], target)
    return nums[m] #the parent function has a dictionary of the indices, which could alternatively be passed into the recursive call

def binRec1(nums: List[int], target, l=0, r=None):
    if r==None: r = len(nums)-1   #I don't like that I have to do this, yet I must
    if l>r: return -1
    m = (l+r)//2
    if target<nums[m]: return binRec1(nums, target, l, m-1)
    if target>nums[m]: return binRec1(nums, target, m+1, r) 
    return m #note that you don't need else because of the return statement


nums = [1, 2, 5, 7, 8, 10, 13, 14, 15, 19]

fn = binRec1
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