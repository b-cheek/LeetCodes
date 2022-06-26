from typing import List
from random import randint
from random import random
from random import shuffle
from math import sqrt

#Binary Search Tree Testing
class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, current, value): #O(log2(n))
        if self.root == None:
            self.root = Node(value) #Add a root if it doesn't already exist
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)

            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)

def visit(node):
    print(node.value)

def preorder(current):
    if not current: return
    visit(current)
    preorder(current.left)
    preorder(current.right)

def inorder(current): #Nodes visited in ascending order
    if not current: return
    inorder(current.left)
    visit(current)
    inorder(current.right)

def postorder(current):
    if not current: return
    postorder(current.left)
    postorder(current.right)
    visit(current)


def iterativePreorderDFT(root):
    stack = [root] #Or start with empty stack and push the root
    while stack:
        node = stack.pop()  #Remove from the stack first
        print(node.value)   #Visit
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)

def iterativeInorderDFT(root):
    stack = []
    node = root
    while (stack or node):
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.value)
            node = node.right

def iterativePostorderDFT(root):
    stack = []
    node = root
    lastNodeVisited = None
    while (stack or node):
        if node:
            stack.append(node)
            node = node.left
        
        else:
            peekNode = stack[-1]    #equivalent to stack.peek() function, I don't like this but it's necessary
            if (peekNode.right and lastNodeVisited != peekNode.right):
                node = peekNode.right
            else:
                print(peekNode.value)
                lastNodeVisited = stack.pop()

def BFS(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        print(node.value)

numsSize = 10
nums = (list(range(0,numsSize)))

for i in range(0, len(nums)):   #This loop will shuffle the numbers so the tree is somewhat balanced
    swapIndex = randint(i, numsSize-1)
    temp = nums[i]              #\
    nums[i] = nums[swapIndex]   # >swap with a random index later in the list 
    nums[swapIndex] = temp      #/

print(nums)

testTree = BST()
for i in nums:
    testTree.add(testTree.root, i)

BFS(testTree.root)

# iterativePostorderDFT(testTree.root)
# print("")
# postorder(testTree.root)

#Generic Tree Testing
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def addNode(node, value, depth):
    if (node.neighbors and random.random()<(1/math.sqrt(depth+1)-0.1)):
        addNode(node.neighbors[random.randint(0, len(node.neighbors)-1)], value, depth+1)
    else:
        node.neighbors.append(TreeNode(value))
        

startNode = TreeNode(0)

numsList = []
for i in range(1,100):
    numsList.append(i)
random.shuffle(numsList)

for i in numsList:
    addNode(startNode, i, 0)

def printBigTree(node, tabString):
    print(tabString, node.value)
    if node.neighbors:
        for i in node.neighbors:
            printBigTree(i, tabString+"\t")

printBigTree(startNode, "")