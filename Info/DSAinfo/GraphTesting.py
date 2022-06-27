from random import random
from random import shuffle
from random import randint
from collections import deque

#OBJECT REPRESENTATION
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def addNode(nodes, value):
    if not nodes:
        nodes.append(GraphNode(value))
        return
    newNode = GraphNode(value)
    for i in nodes:
        if random()>0.9: #The closer this constant is to 1, the more neighbors each node will have
            i.neighbors.append(newNode)
            newNode.neighbors.append(i) #This makes the graph undirected, note that removing it would make the graph directed, but old nodes could never point to new nodes
    nodes.append(newNode)
            
nodes = []

#Creating the graph
numsList = []
for i in range(20): #The more nodes you add, th emore likely the graph is to be connected, depending on random calulation above
    numsList.append(i) #20 is good for small but not connected, 50+ to make connected very likely
shuffle(numsList)

# print(numsList)

for i in numsList:
    addNode(nodes, i)
# This was added to try and make sure the graph is connected, but BFS is often used
# to see if a path exists, so I took this out to allow a path to not exist
# (even though this code doesn't accomplish the goal anyway)
# for i in nodes:
#     if not i.neighbors:
#         neighborIndex = randint(0, len(nodes)-1)
#         i.neighbors.append(nodes[neighborIndex])
#         nodes[neighborIndex].neighbors.append(i)

def printGraph(nodes):
    for i in nodes:
        print(i.value)
        for j in i.neighbors:
            print(j.value, end=", ")
        print('\n')

# printGraph(nodes)

def getRandomNode(nodes):
    return nodes[randint(0, len(nodes)-1)]

def DFS(node, visited): #DEFAULT ARGUMENTS ARE BOUND AT FUNCTION DEFINITION, NOT FUNCITON EXECUTION. Not using prevents the visited list from carrying over from the previous call
    # print(list(map(lambda node: node.value, visited)))
    visited.append(node)
    print(node.value)
    for i in node.neighbors:
        if i not in visited: #Technically doing this check at a different place than the iterative implementations, but is more natural
            DFS(i, visited)
    return visited #This is only for testing!!

def findPath(start, end, visited): #DEFAULT ARGUMENTS ARE BOUND AT FUNCTION DEFINITION, NOT FUNCITON EXECUTION. Not using prevents the visited list from carrying over from the previous call
    # print(start.value, list(map(lambda node: node.value, visited)))
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
    return visited #This is only for testing!!

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
        # print(list(map(lambda node: node.value, list(queue))), list(map(lambda node: node.value, visited)))
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node==end:
                return parents[node] + [node]
            for i in node.neighbors:
                parents[i] = parents[node] + [node]
                queue.append(i)
    return []

    

randNode0 = getRandomNode(nodes)
randNode1 = getRandomNode(nodes)

# printGraph(nodes)
# print(randNode0.value, randNode1.value)


DFS(randNode0, [])
print(findPath(randNode0, randNode1, []))

iterativeDFS(randNode0)
print(iterativeFindPath(randNode0, randNode1))

BFS(randNode0)
print(list(map(lambda node: node.value, shortestPath(randNode0, randNode1))))

# This was originally to see if every vertex was visited, but that's not
# necessarily the point of BFS (see above)
# searchResult = (list(map(lambda node: node.value, DFS(nodes[randint(0, len(nodes)-1)], []))))
# searchResult.sort()
# numsList.sort()
# print(searchResult==numsList)
# print(searchResult)
# print(numsList)

#MATRIX REPRESENTATION

n=5
matrix = [[None]*n for i in range(n)] # note that [[None]*n]*n creates n references to the same list of [None]*n, which caused the error of all the columns being updated at the same time

def printMatrix(matrix):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            print(matrix[row][col], end="\t")
        print()

numsList = []
for i in range(int(n**2/2)): #Half the graph will have nodes
    numsList.append(i)
shuffle(numsList)

for i in numsList: #I though about a more sophisticated algorithm to make nicer graphs, but settled on randomly putting nodes in the matrix
    cell = (randint(0, n-1), randint(0, n-1))
    while matrix[cell[0]][cell[1]]:
        cell = (randint(0, n-1), randint(0, n-1))
    matrix[cell[0]][cell[1]] = i

printMatrix(matrix)


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

matrixDFS(matrix)
matrixBFS(matrix)