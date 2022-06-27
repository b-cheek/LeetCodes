# Missing from this document

* Dijkstra's Algorithm
* Topological Sort
* Probably More

# Object Representation

## Creation

```python
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
```

## Algorithms

### DFS

```python
def DFS(node, visited): #DEFAULT ARGUMENTS ARE BOUND AT FUNCTION DEFINITION, NOT FUNCITON EXECUTION. Not using prevents the visited list from carrying over from the previous call
    visited.append(node)
    print(node.value)
    for i in node.neighbors:
        if i not in visited: #Technically doing this check at a different place than the iterative implementations, but is more natural
            DFS(i, visited)

def findPath(start, end, visited): #DEFAULT ARGUMENTS ARE BOUND AT FUNCTION DEFINITION, NOT FUNCITON EXECUTION. Not using prevents the visited list from carrying over from the previous call
    if start == end: return True
    visited.append(start)
    for i in start.neighbors:
        if i not in visited: #see corresponding comment in DFS
            if findPath(i, end, visited): return True
    return False

def iterativeDFS(start):
    visited = []
    stack = deque([start])
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node.value)
            for i in node.neighbors:
                stack.append(i)

def iterativeFindPath(start, end):
    visited = []
    stack = deque([start])
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node==end: return True
            for i in node.neighbors:
                stack.append(i)
    return False
```

### BFS

```python
def BFS(start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node.value)
            for i in node.neighbors:
                queue.append(i)
    return visited #This is only for testing!!

def shortestPath(start, end): # Note that it is difficult to find the path length without remembering parents in the path. I tried
    parents = {
        start: []
    }
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node==end:
                return parents[node] + [node]
            for i in node.neighbors:
                parents[i] = parents[node] + [node]
                queue.append(i)
    return []
```

# Matrix Representation

## Creation

It's just a 2D arrary of values, I chose to represent empty cells as None, so it may look something like this:

<table>
<tbody>
  <tr>
    <td>None</td>
    <td>10</td>
    <td>None</td>
    <td>None</td>
    <td>4</td>
  </tr>
  <tr>
    <td>None</td>
    <td>1</td>
    <td>None</td>
    <td>2</td>
    <td>None</td>
  </tr>
  <tr>
    <td>None</td>
    <td>5</td>
    <td>None</td>
    <td>7</td>
    <td>11</td>
  </tr>
  <tr>
    <td>None</td>
    <td>None</td>
    <td>9</td>
    <td>8</td>
    <td>6</td>
  </tr>
  <tr>
    <td>3</td>
    <td>None</td>
    <td>None</td>
    <td>None</td>
    <td>None</td>
  </tr>
</tbody>
</table>

## Algorithms

I stole the base of this code [(source)](https://www.techinterviewhandbook.org/algorithms/graph/) so some of it is a bit wonky


```python
def matrixDFS(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0)) #Allows moving to adjacent cells in each direction

  def traverse(i, j):
    if (i, j) in visited or not matrix[i][j]: #I added the not part
      return

    visited.add((i, j))
    print(matrix[i][j])
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols: #Prevent out of bounds error
        # Add in question-specific checks, where relevant.
        #(b-cheek) Usually question-specific stuff occurs at the visiting in the upper loop, not when enqueing neighbors?
        traverse(next_i, next_j)

  #MY CODE  
  cell = (randint(0, len(matrix)-1), randint(0, len(matrix)-1))
  while not matrix[cell[0]][cell[1]]:
      cell = (randint(0, len(matrix)-1), randint(0, len(matrix)-1))
  traverse(cell[0], cell[1])
# Maybe I'll understand why every cell is traversed, but I usually picked a random cell in my other tests (as above)
#   for i in range(rows):
#     for j in range(cols):
#       traverse(i, j)
```

### BFS

```python
def matrixBFS(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0)) #Allows moving to adjacent cells in each direction)

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited and matrix[curr_i][curr_j]: #I added second part
        visited.add((curr_i, curr_j))
        print(matrix[curr_i][curr_j]) #MY CODE
        # Traverse neighbors.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols: #Prevent out of bounds error
            # Add in question-specific checks, where relevant.
            queue.append((next_i, next_j))

#MY CODE
  cell = (randint(0, len(matrix)-1), randint(0, len(matrix)-1))
  while not matrix[cell[0]][cell[1]]:
      cell = (randint(0, len(matrix)-1), randint(0, len(matrix)-1))
  traverse(cell[0], cell[1])
# Same deal as DFS
#   for i in range(rows):
#     for j in range(cols):
#       traverse(i, j)
```