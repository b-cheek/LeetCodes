# Path Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution0:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        if not root.left and not root.right and root.val==targetSum: #Can't just do targetSum==0 for empty case
            return True #putting root.val==targetSum here is significantly slower
        
        targetSum-=root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and val==targetSum: return True
            if node.left: stack.append((node.left, val+node.left.val))
            if node.right: stack.append((node.right, val+node.right.val))
        return False