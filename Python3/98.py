# Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

# This solution recursively checks that each node is a valid BST.
# I originally thought to do this by checking the relation of values with children,
# i.e. node.left.val < node.val < node.right.val.
# However, this solution checks this relation with a node and its ancestors.
# To check that each node is greater than ALL its left children, and less than ALL its right children,
# we store the value of the max left ancestor and min right ancestor as we traverse the tree,
# and if any node is greater than a left ancestor or less than a right ancestor,
# we know the tree is invalid.
# It is important to understand left vs right ancestor:
#   * left ancestor is a node whose RIGHT subtree contains our current node
#   * right ancestor is a node whose LEFT subtree contains our current node
# A good way to understand why we verify from bottom-up instead of top down is to consider the following tree:
#       5
#      / \
#     1   6
#        / \
#       4   7
# In this tree, 4 is greater than 5, but less than 6, so it would pass the top-down check.
# However, 4 is less than 5, so it would fail the bottom-up check.
class Solution0:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left represents the greatest value above and left of node, max left ancestor
        # right represents the smallest value above and right of node, min right ancestor
        def valid(left, node, right): # Note that left and right are numbers, node is the only node
            if not node: return True # base case

            if not left<node.val<right: return False # Check that node is within the ancestor bounds

            # Recursively check children, updating ancestor bounds
            # Updating ancestor bounds happens without any checks, since the ancestor bounds
            # will always be the parent, and the previous bound from the other direction.
            # To prove why the parent becomes the new ancestor bound, let's use a left parent as an example:
            # A child node at least must be greater than a left parent. The same logic applied to that parent,
            # and all the other ancestors, meaning that the child will also be greater than any left ancestor.
            # The bound is actually only defined by the most recent left and right ancestors, but the BST
            # invariant is typically described as a node being greater than ALL left children, so I use that
            # terminology to help explain. We know that the other bound than the direction of the parent
            # must stay the same, since the only difference in ancestors with the parent is the parent itself.
            # Neetcode does a fairly good job explaining, just go watch him.
            return valid(left, node.left, node.val) \
            and valid(node.val, node.right, right)
            
        # Start with ancestor bounds of -inf and inf, root must be valid
        return valid(-inf, root, inf)


# This solution uses the property that inorder DFS of a BST will return a sorted list.
# This solution is simpler imo
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque([])
        lastVal = -inf
        # Note that inorder is LVR.
        while stack or root:
            # To add to the stack without visiting a parent first, we will traverse to the left using root.
            if root:
                stack.append(root)
                root = root.left
            # When we hit the bottom, then we can visit the parent
            else:
                root = stack.pop()
                if root.val<=lastVal: return False # Check that the value of the nodes is always increasing
                lastVal = root.val
                # After visiting the parent, add the right child to the stack (happens in initial if statement)
                root = root.right
        return True