# Number of Islands

# I could spent some more time thinking about placement of when you add to visited,
# but I've already wasted enough time.

# Iterative DFS, each island is like an isolated graph.
# Perform DFS on anywhere there is land, and count the number of unique islands
class Solution0:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inBounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[row])
        visited = set() # Keep track of which cells have been visited
        res = 0 # number of islands
        directions = [(1, 0), (0,1), (-1, 0), (0, -1)] # Traverses to every adjacent cell (no diags)
        # Outer loop, traverses through each cell
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # If not part of island or already visited, don't DFS
                if grid[row][col] == '0' or (row, col) in visited: continue
                # Iterative DFS
                islandStack = deque([(row, col)])
                while islandStack:
                    r, c = islandStack.pop()
                    # Still need to check for water and duplicates
                    if grid[r][c] == '0' or (r, c) in visited: continue
                    visited.add((r, c))
                    for dy, dx in directions:
                        if not inBounds(r + dy, c + dx): continue
                        islandStack.append((r + dy, c + dx))
                res += 1
                # Each time iterative DFS occurs, it starts on undiscovered land and
                # traverses to every connected land, AKA whole island, so increment island count

        return res


# This solution differs mainly by using BFS, but has a few refactors as well
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col): # Abstract into function, reduces nesting
            islandQ = deque([(row, col)])
            visited.add((row, col))
            while islandQ:
                row, col = islandQ.popleft() # Uses queue for DFS
                for dy, dx in directions: # Could put dir array here, but I think naming it is more readable
                    r = row + dy
                    c = col + dx
                    # Check that neighbor is in bounds, land, and undiscovered
                    if r not in range(rows) or c not in range(cols) or \
                    grid[r][c] == '0' or (r, c) in visited: continue
                    islandQ.append((r, c))
                    visited.add((r, c))
                    # Note that unlike DFS, we need to have two different lines where we add a node to visited
                    # You may think to just put the visited statement after line 45.
                    # This is me giving up on explaining this, see top
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0' or (row, col) in visited: continue
                bfs(row, col)
                res += 1

        return res


# This solution uses recursive DFS, it is the most concise and readable imo
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if ( # Use parentheses, each line has individual meaning
                row not in range(rows)
                or col not in range(cols)
                or grid[row][col] == '0'
                or (row, col) in visited
            ): return # return instead of continue, we are recursing
            visited.add((row, col))
            for dy, dx in directions:
                dfs(row + dy, col + dx)
            # Unlike the previous solutions, we add the neighbors before checking
            # bounds etc.

        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0' or (row, col) in visited: continue
                dfs(row, col)
                res += 1

        return res