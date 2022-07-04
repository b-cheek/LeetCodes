# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution0: #I didn't use this solution but see comments
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isMatch(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isMatch(self, root1, root2):
        if not (root1 and root2): #Note De'Morgan's Laws
            return root1 == root2
        if root1.val != root2.val: return False
        return self.isMatch(root1.left, root2.left) and self.isMatch(root1.right, root2.right)

class Solution1:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isMatch(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isMatch(self, root1, root2):
        if (not root1 and not root2): return True
        if (not root1 or not root2): return False
        if root1.val != root2.val: return False
        return self.isMatch(root1.left, root2.left) and self.isMatch(root1.right, root2.right)

