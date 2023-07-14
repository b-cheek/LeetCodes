# Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0: #Pretty simple imo, O(n)?
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        if root.left or root.right:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        return root
            
class Solution1: # S1 but iteratively Also O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node.left or node.right: #There probably is a better way to do the control flow here
                temp = node.left
                node.left = node.right
                node.right = temp
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root

class Solution2: #Did NOT think this would work that well. I still feel like maybe I just got lucky and the testing ran faster
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stack = deque([root])
        while stack:
            node = stack.pop()
            if not node: continue #This is the change, only control flow needed, I though all the adding None to the stack would make it net slower though
            temp = node.left
            node.left = node.right
            node.right = temp
            stack.append(node.left)
            stack.append(node.right)
        return root
            
class Solution3: #I think my theory may have been correct, or for whatevever reason deque is faster popping from the back than the front because this was still pretty slow in testing
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stack = deque([root])
        while stack:
            node = stack.popleft() #BFS WOW!!!! (Last one was DFS)
            if not node: continue 
            temp = node.left
            node.left = node.right
            node.right = temp
            stack.append(node.left)
            stack.append(node.right)
        return root