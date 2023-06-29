# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution0: # Binary search, O(logn)
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while (l<=r):
            m = (l+r)//2 # Only flaw
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1

        return l

class Solution1:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while (l<=r):
            m = l+(r-l)//2 # Prevent overflow, wasn't necessary on lc though because max size is 2^64
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1

        return l