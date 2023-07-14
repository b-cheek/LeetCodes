# Find Smallest Letter Greater Than Target

class Solution0:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

class Solution1: #weird binSearch
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r, = 0, len(letters)
        while l<r:
            m = l + (r-l)//2
            if ord(letters[m])<=ord(target): l = m+1 # Note you DON'T HAVE TO use ord(), just letters[m]<target would suffice, but ord is faster?
            else: r = m
        return letters[l%len(letters)]

class Solution2: #normal binsearch, do note the greater than or equal to though
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            
            if  target >= letters[mid]: # in binary search this would be only greater than
                low = mid+1
            
            else:
                high = mid-1
                
        return letters[low]