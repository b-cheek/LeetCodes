# Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root1 into root2
        if not (root1 or root2): return None
        if root1 and root2:
            root2.val += root1.val
            root2.left = self.mergeTrees(root1.left, root2.left)
            root2.right = self.mergeTrees(root1.right, root2.right)
        elif root1: return root1
        return root2

class Solution1: #Slightly more confusing, but better control flow
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root1 into root2
        if root1:
            if root2:
                root2.val += root1.val
                root2.left = self.mergeTrees(root1.left, root2.left)
                root2.right = self.mergeTrees(root1.right, root2.right)
                return root2
            return root1
        if root2: return root2
        return None

class Solution2: #This is the real simple version, also note that I am merging root2 into root1 this time
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root2 into root1
        if not root1: return root2
        if not root2: return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
        
class Solution3: #Iterative DFS, doesn't seem to be ideal though
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root2 into root1
        if not root1: return root2
        #Don't need to check root2 because it will return properly anyway
        stack = [[root1, root2]] #This is pretty novel imo
        while stack:
            node = stack.pop()
            if not (node[0] and node[1]): #If they don't both have vals
                continue
            node[0].val += node[1].val
            
            if not node[0].left: #Left child
                node[0].left = node[1].left
            else:
                stack.append([node[0].left, node[1].left]) #Basically the recursive call
            
            if not node[0].right: #repeat above block for right child
                node[0].right = node[1].right
            else:
                stack.append([node[0].right, node[1].right])
                
        return root1

#NOTE: I think the iterative solutions below are basically the same, switching from stack to queue really just changes order.

class Solution4: #Same as above, but with deque
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root2 into root1
        if not root1: return root2
        #Don't need to check root2 because it will return properly anyway
        from collections import deque
        stack = deque([[root1, root2]]) #This is pretty novel imo
        while stack:
            node = stack.pop()
            if not (node[0] and node[1]): #If they don't both have vals
                continue
            node[0].val += node[1].val
            
            if not node[0].left: #Left child
                node[0].left = node[1].left
            else:
                stack.append([node[0].left, node[1].left]) #Basically the recursive call
            
            if not node[0].right: #repeat above block for right child
                node[0].right = node[1].right
            else:
                stack.append([node[0].right, node[1].right])
                
        return root1

#Based on https://leetcode.com/problems/merge-two-binary-trees/discuss/588123/~100.00-fast-in-run-time-and-memory-RecursiveIterativeBFSDFS
class Solution5: #Similar to stack. I moved a check from in loop to out of loop, and chose 2 queues rather than a 2d queue
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: #I will merge root2 into root1
        if not root1: return root2
        if not root2: return root1
        
        from collections import deque
        q1 = deque([root1]) #I chose to use 2 queues rather than a 2D q similar to the 2D stack above
        q2 = deque([root2])
        
        while (q1):
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            node1.val += node2.val
            
            if not node1.left:
                node1.left = node2.left
            elif node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            
            if not node1.right:
                node1.right = node2.right
            elif node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
                
        return root1
