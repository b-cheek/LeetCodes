# Minimum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution0: #BFS
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = [root]
        root.depth = 1 #I assign a member to each node, so when the child nodes are put on the queue they can be 1 + parent.depth
        while queue:
            node = queue.pop(0)
            if not (node.left or node.right): return node.depth
            if node.left: 
                temp = node.left #This is necessary using member stuff
                temp.depth = node.depth + 1
                queue.append(temp)
            if node.right:
                temp = node.right
                temp.depth = node.depth + 1
                queue.append(temp)

class Solution1: #Optimized using a deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        from collections import deque
        queue = deque([root])
        root.depth = 1
        while queue:
            node = queue.popleft()
            if not (node.left or node.right): return node.depth
            if node.left: 
                temp = node.left
                temp.depth = node.depth + 1
                queue.append(temp)
            if node.right:
                temp = node.right
                temp.depth = node.depth + 1
                queue.append(temp)

class Solution2: #Optimized from discussion
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = collections.deque([(root, 1)]) #Using a tuple eliminates need for temp variable
        while queue:
            node, depth = queue.popleft()
            if node: #Add empty nodes and check at beginning instead of writing two checks for node.left and right
                if not node.left and not node.right: return depth
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

class Solution3: #DFS, did not consider this
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 #basic recursive step
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # Using max because if the previous if is skipped there is either
        # One child: this means not a leaf, so the empty child (and smaller depth) is invalid
        # No children: L and R depth are equivalent, so returns 0