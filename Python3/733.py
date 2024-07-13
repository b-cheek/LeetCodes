# Flood Fill

from collections import deque

## Just a little note for this solution, thought process here applies to others as well.
## I wanted to have tileColor in the loop because I was thinking,
## "In an irl implementation I would want to base it off how close the color is to the current tile"
## I realize now that this would require a visted array anyway, it is probably not how you would
## Want to do it because it would fill a gradient. Oh well.

## Note the existence of better solutions like span filling that are beyond the scope of the question.
## Also note using a structure to store adjacent cell offsets

class Solution0: ## Iterative BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color==image[sr][sc]: return image

        tileColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        floodq = deque([(sr, sc)])
        
        while floodq:
            tile = floodq.popleft()

            if tile[0]+1<m and image[tile[0]+1][tile[1]] == tileColor:
                floodq.append((tile[0]+1, tile[1]))

            if tile[1]+1<n and image[tile[0]][tile[1]+1] == tileColor:
                floodq.append((tile[0], tile[1]+1))

            if tile[0]-1>=0 and image[tile[0]-1][tile[1]] == tileColor:
                floodq.append((tile[0]-1, tile[1]))

            if tile[1]-1>=0 and image[tile[0]][tile[1]-1] == tileColor:
                floodq.append((tile[0], tile[1]-1))

            image[tile[0]][tile[1]] = color

        return image

class Solution1: ## Same except DFS using stack. See visual demo! (https://en.wikipedia.org/wiki/Flood_fill#Moving_the_recursion_into_a_data_structure)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color==image[sr][sc]: return image

        tileColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        floodq = deque([(sr, sc)])

        while floodq:
            tile = floodq.pop() ## The only changed line

            if tile[0]+1<m and image[tile[0]+1][tile[1]] == tileColor:
                floodq.append((tile[0]+1, tile[1]))

            if tile[1]+1<n and image[tile[0]][tile[1]+1] == tileColor:
                floodq.append((tile[0], tile[1]+1))

            if tile[0]-1>=0 and image[tile[0]-1][tile[1]] == tileColor:
                floodq.append((tile[0]-1, tile[1]))

            if tile[1]-1>=0 and image[tile[0]][tile[1]-1] == tileColor:
                floodq.append((tile[0], tile[1]-1))

            image[tile[0]][tile[1]] = color

        return image

class Solution2: ## Recursize DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color==image[sr][sc]: return image

        tileColor = image[sr][sc]
        m = len(image)
        n = len(image[0])

        def dfs(r, c):
            if image[r][c]==tileColor:
                image[r][c] = color ## Note that this has to be done before recursion
                if r+1<m: dfs(r+1, c)
                if c+1<n: dfs(r, c+1)
                if r-1>=0: dfs(r-1, c)
                if c-1>=0: dfs(r, c-1)

        dfs(sr, sc)

        return image