from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            print(i)
            for j in range(0, m+n):
                print(str(nums1[j])+ " ", end='')
                if i<nums1[j]:
                    nums1.insert(j, i)

class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n>0:
            if m>0:
                for i in range(0, n):
                    index = m + i - 1
                    while(index>=0):
                        if nums2[n-i-1]>=nums1[index]:
                            nums1[index+1] = nums2[n-i-1]
                            index = -2
                        else:
                            nums1[index+1] = nums1[index]
                        index-=1
                    if index==-1: nums1[0] = nums2[n-i-1]
            else:
                for i in range (0, n):
                    nums1[i] = nums2[i]


        

arr1 = [2, 0]
arr2= [1]
Solution1().merge(arr1, len(arr1)-len(arr2), arr2, len(arr2))
print(arr1)

