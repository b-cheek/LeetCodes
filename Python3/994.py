# Rotting Oranges

# BFS, pretty straightforward I just couldn't get it :(
class Solution0:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenQ = deque([]) # Q will only ever hold rotten oranges
        fresh = 0 # Keep track of fresh oranges
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows): # Add all rotten oranges to queue; rot expands out from these
            for col in range(cols):
                if grid[row][col]==2: rottenQ.append((row, col))
                if grid[row][col]==1: fresh += 1 # Count fresh oranges

        minutes = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Go until rot can't spread any more, or no more fresh oranges
        # You may think that we can just wait until the rot stops spreading,
        # but then 
        while rottenQ and fresh:
            # This for loop is a trick to allow us to count the BFS level
            # Our q starts with all rotten oranges, so in first iteration of 
            # the for loop we visit just the initial rotten oranges.
            # Since they are all popped, and the new rotten oranges are added to the end,
            # we repeat this, and each for loop is a BFS level, and a minute.
            for _ in range(len(rottenQ)):
                row, col = rottenQ.popleft()
                for dy, dx in directions:
                    r = row + dy
                    c = col + dx
                    # If a neighbor is in bounds and fresh
                    if (r in range(rows)
                        and c in range(cols)
                        and grid[r][c]==1
                    ):
                        grid[r][c] = 2 # Rot it
                        fresh -= 1 # Update fresh count
                        rottenQ.append((r, c)) # Add to rotten queue

            minutes += 1
            
        # If there are still fresh oranges, return -1, otherwise return minutes
        return minutes if not fresh else -1