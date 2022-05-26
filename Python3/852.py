class Solution0: #third accepted solution
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while True:
            i=(l+r)//2
            if arr[i]>arr[i-1]:
                if arr[i]>arr[i+1]: return i
                l=i
            else: r=i

class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def peakIndexInMountainArray(self, arr: List[int]) -> int:
            return self.peakIndexRecursive(arr, 0, len(arr)-1)
                    
        def peakIndexRecursive(self, arr, l, r):
            m = (l+r)//2
            if arr[m]>arr[m-1]:
                if arr[m]>arr[m+1]: return m
                return self.peakIndexRecursive(arr, m+1, r)
            return self.peakIndexRecursive(arr, l, m)