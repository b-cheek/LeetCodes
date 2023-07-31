# Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# My original failed attempt to solve P235 not realizing it was for SEARCH tree.
# Basically DFS tracking parent chain, but for performed on each node, and not working.
# Not going to figure out the problem, just for historical reference.
# Note that this is not on my sheet.
class Solution0:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def containsNodes(root):
            pFound = qFound = False
            nodeStack = deque([root])
            while nodeStack and not (pFound and qFound):
                node = nodeStack.pop()
                if not node: continue
                if node is p: pFound = True
                elif node is q: qFound = True
                nodeStack.append(node.left)
                nodeStack.append(node.right)
            
            return len(nodeStack)>0

        if containsNodes(root.left): return self.lowestCommonAncestor(root.left, p, q)
        elif containsNodes(root.right): return self.lowestCommonAncestor(root.right, p, q)
        else: return root


# This solution uses recursive preorder(?) DFS to find the parent chain for each node, then compares the chains.
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfsParents(root, node, parents): # helper function, returns the parent chain of target node if found, None otherwise
            if not root:
                return None
            if root is node:
                return parents + [node] # Note that this line is because each node is a parent of itself
            # If node is found in left tree return the chain, else if found in right tree return the chain, else return None
            return dfsParents(root.left, node, parents + [root]) \
            or dfsParents(root.right, node, parents + [root])

        pParents = dfsParents(root, p, [root])
        qParents = dfsParents(root, q, [root])

        resIdx = 0
        # Iterate through the ancestors of each node until divergence
        while resIdx<len(pParents) and resIdx<len(qParents) \
        and pParents[resIdx] == qParents[resIdx]:
            resIdx += 1

        # Since we iterate PAST LCA, return previous node
        return pParents[resIdx - 1] # Choice of pParents is arbitrary, since all ancestors through resIdx - 1 are the same


# Recursive postorder DFS while tracking LCA as you go up the tree.
# There's probably a better way to explain this, but I won't waste time.
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorderDFS(node):
            if not node: # Base case
                return None
            # The inLeft and inRight variables are dual-purpose:
            # As their names imply, they are truthy if the target node is found in the left or right subtree,
            # and falsey otherwise.
            # The second purpose is that they store the actual value of the LCA in each tree.
            inLeft = postorderDFS(node.left)
            inRight = postorderDFS(node.right)
            # The following if statement covers 2 cases where the node is LCA:
            #   1. One node is in the subtree of another
            #   2. Neither node is the parent of the other
            # In case 1, since we are traversing bottom up (postorder), the latter node is the parent of the other
            # and thus will be returned. In case 2, "inLeft and inRight" is only possible for the LCA, so it will be returned.
            if node is p or node is q or (inLeft and inRight): # Don't need to calculate inLeft and inRight for case 1, see S3
                return node
            return inLeft or inRight # If the node isn't the LCA, flow up the LCA if it exists (return None otherwise)

        return postorderDFS(root) # I should have realized that helper is unnecessary


# Essentially same as S2 with some improvements that also make it more concise.
# I would normally say this is less readable, but I struggled to explain S2 anyway
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root # Covers the "if not node" and "if node is p or q" cases from S2
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right # Covers the "inLeft and inRight" and "inLeft or inRight" cases from S2