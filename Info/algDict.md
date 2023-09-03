# Algorithm Reference

This document contains a collection of algorithms that are standard knowledge for an interview, but I seem to keep forgetting or having trouble with. This was inspired by binary search and insertion.

Note that this is somewhat against the ethos that keywordDict follows, as it is actually being tested and not a language-specific thing. I consider this a fallback when I give up, and a reference for me to stay consistent in implementing these hopefully.

## Binary Search

```python
class Solution0: #iterative
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r: ## Yes, <= is necessary
            m = (l+r)//2 ## Rewrite as m = l+(r-l)//2 to avoid overflow. Not necessary here, but LOOK AT CONSTRAINTS!
            if target<nums[m]:
                r = m-1
            elif target>nums[m]:
                l = m+1
            else:
                return m
        return -1

class Solution1:    #recursive
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(self, nums: List[int], l: int, r: int) -> int:
            if l>r: return -1
            m = (l+r)//2
            if target<nums[m]:
                return binSearch(self, nums, l, m-1)
            elif target>nums[m]:
                return binSearch(self, nums, m+1, r)
            return m
        
        return binSearch(self, nums, 0, len(nums)-1)
```

## Binary Insertion (insort with bisect)

See [cpython source](https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L15-L35) for the `bisect` module.

```python
def insort_right(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    lo = bisect_right(a, x, lo, hi)
    a.insert(lo, x)

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
```
