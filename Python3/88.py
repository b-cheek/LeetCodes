# Merge Sorted Array

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

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0: return nums1
        n1 = 0
        n2 = 0
        print(m, n)
        while (n1<m+n2):
            print("OUTER", nums1[n1], nums2[n2])
            if nums1[n1] > nums2[n2]:
                for push in range (m+n2, n1, -1):
                    print("INNER", nums1, push)
                    nums1[push] = nums1[push-1]
                nums1[n1] = nums2[n2]
                if n2==n-1: return nums1
                n2+=1
            n1+=1
        for empty in range (n1, m+n):
            nums1[empty] = nums2[n2]
            n2+=1

class Solution3: #found in discussion, good time complexity
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


class Solution4:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        writeIndex = m + n - 1
        m, n = m-1, n-1
        
        while n>=0 and m>=0:
            if nums1[m] > nums2[n]:
                nums1[writeIndex] = nums1[m]
                #nums1[m] = float("-inf")           We don't need to change this value because m will be pointing to m-1
                m -= 1
            else:
                nums1[writeIndex] = nums2[n]
                n -= 1
            writeIndex -= 1
            
        if n>-1:
            nums1[0:n+1] = nums2[0:n+1]

# arr1 = [1,2,3,0,0,0]
# arr2= [2,5,6]
arr1 = [2, 0]
arr2= [1]
Solution2().merge(arr1, len(arr1)-len(arr2), arr2, len(arr2))
print(arr1)

