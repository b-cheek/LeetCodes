class Solution0:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r, = 0, len(letters)
        while l<r:
            m = l + (r-l)//2
            if ord(letters[m])<=ord(target): l = m+1 # Note you DON'T HAVE TO use ord(), just letters[m]<target would suffice, but ord is faster?
            else: r = m
        return letters[l%len(letters)]