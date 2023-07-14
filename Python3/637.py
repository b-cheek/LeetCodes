# Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0: #depth first
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        countPerLevel = []
        res = []
        self.average(root, 0, res, countPerLevel)
        for i in range(0, len(res)):
            res[i]=res[i]/countPerLevel[i]
        return res
            
    def average(self, node, level, total, countPerLevel):
        if not node:
            return
        if (level<len(total)):
            total[level] += node.val
            countPerLevel[level] += 1
        else:
            total.append(node.val)
            countPerLevel.append(1)
        self.average(node.left, level+1, total, countPerLevel)
        self.average(node.right, level+1, total, countPerLevel)

class Solution0: #breadth first
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        while queue:
            total = count = 0
            temp = []
            while queue:
                node = queue.pop() #actually a stack :(
                total += node.val
                count += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            res.append(total/count)
        return res

class Solution2: #breadth first from discussion
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        
        while queue:
            size = len(queue)
            total = 0
            for i in range(0, size):
                node = queue.pop(0)
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(total/size)
        return res