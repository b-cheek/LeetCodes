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

#Code adapted from https://leetcode.com/problems/subtree-of-another-tree/discuss/474425/JavaPython-2-solutions%3A-Naive-Serialize-in-Preorder-then-KMP-O(M%2BN)-Clean-and-Concise
class Solution2: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root): #Turn tree into a string so you can search it that way with kmp (preorder serialization)
            if root == None:
                return ",#" #The comma is necessary to distinguish between two digit numbers and two one digit numbers
            
            return "," + str(root.val) + serialize(root.left) + serialize(root.right)
        
        def getLPS(s): #See KMP algorithm in string matching
            m = len(s)
            j = 0
            lps = [0] * m
            for i in range(1, m):
                while s[i] != s[j] and j > 0: j = lps[j-1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        def kmp(s, p):
            lps = getLPS(p)
            n, m, j = len(s), len(p), 0
            for i in range(n):
                while s[i] != p[j] and j > 0: j = lps[j-1]
                if s[i] == p[j]:
                    j += 1
                    if j == m: return True
            return False
            
        return kmp(serialize(root), serialize(subRoot))

#Code adapted from https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S+T)-approaches)/1173819
class Solution3:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from hashlib import sha256
        def hashify(node): #In a way, turning a node into a hash is like serialization, but hash always has 64 chars so can be better for large trees?
            node = node.encode('utf-8') 
            S = sha256()
            S.update(node)
            return S.hexdigest()
        
        def hashTree(t, hs): #Modifies an empty set input IN PLACE to add hashes for each node
            if not t:
                return '#'
            t_hash_value = hashify(hashTree(t.left, hs)+str(t.val)+hashTree(t.right, hs)) #Inorder cryptographic serialization
            hs.add(t_hash_value)
            return t_hash_value #Used within recursive step of the function
            
            
        treeHashset = set() #A hashset is used for efficient lookup, a hash could also be assigned as a member for each node, and then use dfs to see if the subtree hash matches any of the node hashes
        hashTree(root, treeHashset)
        return hashTree(subRoot, set()) in treeHashset #Note that the use of in implements some level of string matching natively, and we could do it ourselves with kmp