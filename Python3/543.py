import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthOfBinaryTree(root: Optional[TreeNode]) -> int: #note, depth is the number of edges along the unique path between a node and the root node of a tree
            if not root: return 0
            return 1 + max(depthOfBinaryTree(root.left), depthOfBinaryTree(root.right))
        
        if not root: return 0
        return max(depthOfBinaryTree(root.left) + depthOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
                    #^This part measures if the path going through the root is greater, ^This part checks to see if the diameter of either subtree is

class Solution1: #This is basically the same as Solution0, but uses a stack
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthOfBinaryTree(root: Optional[TreeNode]) -> int:
            if not root: return 0
            return 1 + max(depthOfBinaryTree(root.left), depthOfBinaryTree(root.right))
        
        stack = collections.deque([root])
        maxDiameter = 0
        while stack:
            node = stack.pop()
            if not node: continue
            maxDiameter = max(maxDiameter, depthOfBinaryTree(node.left) + depthOfBinaryTree(node.right))
            stack.append(node.left)
            stack.append(node.right)
        return maxDiameter
        
class Solution2: #This solution implements some pruning, but still is slow, idk why
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthOfBinaryTree(root: Optional[TreeNode]) -> int:
            if not root: return 0
            return 1 + max(depthOfBinaryTree(root.left), depthOfBinaryTree(root.right))
        
        stack = collections.deque([root])
        maxDiameter = 0
        while stack:
            node = stack.pop()
            if not node: continue
            leftNodeDepth = depthOfBinaryTree(node.left)
            rightNodeDepth = depthOfBinaryTree(node.right)
            maxDiameter = max(maxDiameter, leftNodeDepth + rightNodeDepth)
            if leftNodeDepth>=rightNodeDepth: stack.append(node.left) #This and following line make it so nodes that definitely don't contain a deeper subtree aren't added
            else: stack.append(node.right)
        return maxDiameter

class Solution3: #Evaluate best depth as you scan with depth function
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        
        def depth(root):
            if not root: return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR) #This allows you to track the best as you calculate depths
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best