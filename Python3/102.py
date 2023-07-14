# Binary Tree Level Order Traversal

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS withe queue, keep track of level
class Solution0: # O(n) time, O(n) space
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        res = []
        while q:
            node, level = q.popleft()
            if not node: continue
            if level>len(res)-1: res.append([])
            res[level].append(node.val)
            q.append((node.left, level+1))
            q.append((node.right, level+1))

        return res


# Optimize by keeping track of how many nodes per level, removing need to store depth.
# Since we know top level has only one node, 
class Solution: # O(n) time, O(n) space
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q: # Each iteration is a level of the tree
            level = []
            # Before visiting, the length of the q is the number of nodes in the current level.
            # With the for loop, we can visit only the nodes in the current level without tracking depth.
            for _ in range(len(q)): # Each iteration is a node in the level
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level: res.append(level) # Don't append if the level is empty

        return res