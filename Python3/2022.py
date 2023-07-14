# Convert 1D Array Into 2D Array

class Solution0: #O(n)
    from collections import deque
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original): return []
        ogdq = deque(original)
        new = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                new[i][j] = ogdq.popleft() #Throws numbers from the original into the new 2D aray
        return new

class Solution1: #O(n)
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original): return []
        new = [[0 for i in range(n)] for i in range(m)]
        row = col = i = 0 #Don't like how many variables I had to use but I feel it makes it readable
        while row < m: #slightly more elegantly does solution0
            if col < n:
                new[row][col] = original[i]
                col += 1
                i += 1 #We move to next OG element only when we add an element to the 2D arr
            else: #When we hit the end of one of the subarrays
                col = 0
                row += 1
        return new
            
class Solution2:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) == m*n: # a slightly smarter way to do this check than above and below sols?
            for i in range(0, len(original), n): 
                ans.append(original[i:i+n]) #I am mad I didn't think of using array slices
        return ans 

class Solution3: #basically same as sol2
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original): return []
        res = [[0 for i in range(n)] for i in range(m)]
        for i in range(len(original)):
            res[i//n][i%n] = original[i] #Smart
        return res

class Solution4: #Basically Sol2 without slicing
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) == m * n:
            for row in range(m):
                ans.append([])
                for col in range(n):
                    ans[-1].append(original[row * n + col]) #Didn't know you could front append like this
        return ans