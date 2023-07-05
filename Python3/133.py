"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Recursive DFS, track visited nodes with a dictionary[node value] == clone node
class Solution0: # O(E + V) because we visit each node (main dfs) and edge (for loop through neighbors) once
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node: 'Node', visited: dict) -> 'Node':
            if not node: return None
            # The following line works because we are using pointers.
            # Even though the value in dict doesn't have all its neighbors yet, when it is updated
            # the pointer will still point to it
            if node.val in visited: return visited[node.val]
            nodeClone = Node(node.val)
            visited[node.val] = nodeClone
            for neighbor in node.neighbors:
                nodeClone.neighbors.append(helper(neighbor, visited))
            return nodeClone

        return helper(node, {})


# Same as above with some slight readability improvements
class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Move edge case outside helper since for loop won't iterate over nodes of none, 
        # so we just need to check that the input is not none
        if not node: return None
        visited = {} # Move dict out of helper so we don't have to pass it around

        def helper(node: 'Node') -> 'Node':
            if node in visited: return visited[node]
            nodeClone = Node(node.val)
            visited[node] = nodeClone # Use node as key instead of node.val
            # Note that we can do the above because class obj has default hash function.
            for neighbor in node.neighbors:
                nodeClone.neighbors.append(helper(neighbor))
            return nodeClone

        return helper(node)