# Maximum Depth of Binary Tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = deque([(root, 1)]) #Root is at depth of 1, 0 is if no root
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            if not node: continue #This is simpler imo, but it's just slower because I'm adding and removing empty nodes to the stack
            maxDepth = max(maxDepth, depth)
            stack.append((node.left, depth+1))
            stack.append((node.right, depth+1))
        return maxDepth

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root, 0)]) #Root starts at 0, because the final depth variable is the depth None, which is depth of parent+1, so we get depth of the parent by starting at 0, one less than what the depth of the root should be
        while q:
            node, depth = q.popleft()
            if not node: continue #slow, see above
            q.append((node.left, depth+1))
            q.append((node.right, depth+1))
        return depth #Since we are essentially doing the same as Solution1 and BFS and DFS both traverse every node exactly once, BFS is faster because it does not need to check the max every iteration, only the end

class Solution3: #Fixed error from Solution1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = deque([(root, 1)]) #Root is back to starting at one, since None is no longer appended to the stack, so maxDepth is only changed for real nodes
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left: stack.append((node.left, depth+1))
            if node.right: stack.append((node.right, depth+1))
        return maxDepth

class Solution4: #Fixed error from Solution2
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root, 1)]) #Since None children aren't appended to the queue, the final depth will be accurate to a real node, so depth can now start at 1 where it should
        while q:
            node, depth = q.popleft()
            if node.left: q.append((node.left, depth+1))
            if node.right: q.append((node.right, depth+1))
        return depth