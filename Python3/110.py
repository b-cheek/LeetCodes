# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution0: # O(n^2)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            return 1 + max(height(node.left), height(node.right))

        if not root: return True # Edge case

        # Check that root is balanced
        return abs(height(root.left)-height(root.right))<=1 and \
        self.isBalanced(root.left) and self.isBalanced(root.right) # Check that kids are balanced recursively

class Solution1: # O(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # This helper calculates height through postorder dfs; (postorder last because need to visit kids before parent)
        # The height of children flows up to the parents in teh same way as old height fn.
        # However, the height of parent is set to -1 if imbalanced, which flows up the tree.
        def dfsHeight(node):
            if not node: return 0 # From old height fn
            
            # Find left and right heights
            leftHeight = dfsHeight(node.left)
            if leftHeight == -1: return -1 
            rightHeight = dfsHeight(node.right)
            if rightHeight == -1: return -1

            if abs(leftHeight-rightHeight)>1: return -1 # If imbalanced
            return max(leftHeight, rightHeight) + 1 # From old height fn

        return dfsHeight(root) != -1

class Solution1: # O(n) iterative
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        node = root
        last = None
        heights = {}

        # Iterative postorder traversal
        # Note how this is different because it needs a node variable.
        # This is necessary for postorder and inorder, because unlike preorder,
        # the parent is not visited first, and you still need a way to add children
        # To the stack without visiting the parent.
        # This is accomplished by the node variable, which is used to traverse the tree
        # and add nodes to the stack without visiting any nodes.
        # This is most complicated for postorder, since it is the only traversal
        # where you must access a sibling before the parent (LRV).
        # This means when you do reach the parent, you need to check if its kids have been visited
        #
        #               P
        #              / \
        #             L   R
        #
        # value of node: P -> L -> None -> L (visit) -> R -> None -> R (visit) -> P (visit)
        # This is a little tough to truly get. Maybe just try and remember pseudocode
        #
        while stack or node:
            if node: # If there is a left child to visit
                stack.append(node)
                node=node.left # Left
                # Note that you don't have to check if left was just visited like you do for right.
                # This is because the value of node gets set to none after a node is visited,
                # so this for loop won't run

            else: # You've hit the bottom (child of a leaf), or you just visited a node

                # If There is a right child you didn't just visit (prevent loop)
                node = stack[-1] # access the parent so you can view the sibling
                if node.right and last != node.right:
                    node = node.right # Right

                else: # No children to visit, so visit node
                    node = stack.pop() # Visit

                    # Check if balanced: since postorder, L and R are always visited (and only once) before parent
                    left = heights.get(node.left, 0)
                    right = heights.get(node.right, 0)
                    if abs(left-right) > 1: return False # allows immediate return without recursive propagation to root
                    heights[node] = max(left, right) + 1 # Store height to be used by parent

                    last = node # Used to check if a right node was just visited
                    node = None # Ensures that the left node is not revisited
        return True # If the loop completes, all nodes have been visited and confirmed to be balanced
