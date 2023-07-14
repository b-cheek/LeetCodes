# Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution0: ## Recursive
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val:
            if q.val<root.val: return self.lowestCommonAncestor(root.left, p, q)
            else: return root
        if p.val>root.val:
            if q.val>root.val: return self.lowestCommonAncestor(root.right, p, q)
            else: return root
        else: return root

class Solution1: ## Iterative
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val<p.val and root.val<q.val:
                root = root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else: return root

class Solution2: #S1 refactored. Not on sheet, it seems that the double comparison (<>) is slow (2023 update it shouldnt be?)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val<root.val>q.val: #note that although this is less readable than p.val<q.val<root.val, it does NOT mean the same thing. Code!=Math
                root = root.left        # 2023 update Idk what I was getting at here, the math works out the same.
            elif p.val>root.val<q.val:
                root = root.right
            else: return root

class Solution3: ## S0 refactored. This or S ideal imo
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root.val<p.val and root.val<q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            if root.val>p.val and root.val>q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else: return root

## All these solutions are O(n) I believe
## I'm still unsure about the readability of comparison chaining, but I guess it's decent practice.