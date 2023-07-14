# 01 Matrix

class Solution0: # O(m*n) time, O(m*n) space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(mat), len(mat[0])

        # This solution iterates through the matrix in two different directions:
        # first from top left to bottom right, then from bottom right to top left.
        # If we did all the directions, there would be a loop

        # First, we iterate from top left to bottom right
        for row in range(m):
            for col in range(n):
                if dp[row][col] == 0: continue # Since the distance to a 0 is 0, we can use the existing value since we copied mat.
                min_neighbor = inf
                if row>0: # If neighbor is in bounds
                    min_neighbor = min(min_neighbor, dp[row-1][col]) # Check already computed neighbors (opposite to direction of motion)
                if col>0:
                    min_neighbor = min(min_neighbor, dp[row][col-1]) 
                dp[row][col] = min_neighbor + 1
                
        # Then, we iterate from bottom right to top left
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if dp[row][col] == 0: continue
                min_neighbor = inf
                if row<m-1:
                    min_neighbor = min(min_neighbor, dp[row+1][col])
                if col<n-1:
                    min_neighbor = min(min_neighbor, dp[row][col+1])
                dp[row][col] = min(dp[row][col], min_neighbor + 1) # only change if shorter than the first pass

        return dp

# Since all that really matters is whether something is 0 or not,
# the property of line 13 can be extended to the idea that our result will function the same as the input,
# since the 0s stay the same and nothing else can become a 0.
# Because of this we can operate on the matrix in place.
# There are also some tweaks for readability.
class Solution1: # O(m*n) time, O(1) space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0: continue
                top = mat[row-1][col] if row>0 else inf
                left = mat[row][col-1] if col>0 else inf
                mat[row][col] = min(top, left) + 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if mat[row][col] == 0: continue
                bottom = mat[row+1][col] if row<m-1 else inf
                right = mat[row][col+1] if col<n-1 else inf
                mat[row][col] = min(mat[row][col], bottom+1, right+1)

        return mat

# This solution uses BFS from all the 0 nodes, I think this is the intuitive solution and still pretty fast
class Solution2: # O(m*n) time, O(m*n) space for the queue
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        q = deque([])
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = -1 # Mark non zero nodes as -1 until they are visited
                    # Although the idea from line 34 still technically applies,
                    # this is necessary because we are now moving in all directions,
                    # so an infinite loop would happen otherwise

        def inRange(row, col):
            return 0<=row<m and 0<=col<n

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not inRange(nr, nc) or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[row][col] + 1
                q.append((nr, nc))

        return mat