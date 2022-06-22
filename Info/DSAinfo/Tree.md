<!---
# Terminology

* *Root* - the top node in the tree
* *Neighbor* - A node that is directly linked to another
* *Parent* - a neighbor above
* *Child* - a neighbor below
* *Ancestor* - A node reachable by traversing its parent chain
* *Descendant* - A node in the node's subtree
* *Sibling* - Nodes that share a parent
* *Leaf* - A node with no children
* *Interior Node* - A node with children
* *Degree* - Number of children of a node
* *Degree* of a tree - Maximum degree of nodes in the tree
* *Distance* - Number of edges along the shortest path between two nodes
* *Level/Depth* - Number of edges along the unique path between a node and the root node
* *Height* - Maximum number of edges between a node and a leaf
* *Width* - Number of nodes in a level
* *Forest* - A collection of trees

Note:

* UC San Diego Video describes *Level/Depth* and *Height* as starting at one rather than 0.
--->

# Binary Search Tree (BST)

**Binary Tree**: Each node has no more than 2 child nodes  
**Binary Search Tree**: on any subtree, the left node < the root node < all of the right nodes

Note:

* Trees can be balanced or unbalanced
  * Generally, balanced tree operations have a time complexity of O(log2(n)), whereas unbalanced trees are O(n)
* BSTs can not have duplicate values
* [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (Not necessarily a BST)
  * Code
  * Math
  * Linguistics
* Other cool tree types:
  * AVL Trees
  * Red-Black Trees
  * B-Trees
* If a tree has n nodes, it will always have one less number of edges (n-1)

## Creation

```python
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
```

## Traversal

### Depth-First

Here's a cool representation on [Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search) ![image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sorted_binary_tree_ALL_RGB.svg/440px-Sorted_binary_tree_ALL_RGB.svg.png)  
Depth-first traversal (dotted path) of a binary tree:  
*Pre-order (node visited at position red* 🔴): F, B, A, D, C, E, G, I, H;  
*In-order (node visited at position green* 🟢): A, B, C, D, E, F, G, H, I;  
*Post-order (node visited at position blue* 🔵): A, C, E, D, B, H, I, G, F.

I find the following representation to be easier though:  
V: Visit  
L: Go Left  
R: Go Right  

Preorder: VLR  
Inorder: LVR  
Postorder: LRV

The way I remember this is that "L" is always before "R," and the prefix before "order" determines the position of "V"

```python
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
```

It should be noted that this algorithm can also be performed iteratively, using a stack data structure to operate similarly to the call stack in the recursive function. For simplicity, a python list will be used

```python
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
```

<!---
Note:

* For a traversal of a more general graph, make sure to use some isVisited flag for DFS and BFS to avoid any infinite loops
* Preorder traversal is used to create a copy of a tree, since ...?
* Postorder traversal is used to delete a tree, since it frees up the child nodes then the parent node
--->

### Breadth-First

[Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search)

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Sorted_binary_tree_breadth-first_traversal.svg/330px-Sorted_binary_tree_breadth-first_traversal.svg.png)

This would print the nodes in the order: F BG ADI CEH (by level)

The implementation has some similarities to iterative depth-first traversal, but uses a queue instead of a stack. For this reason, it does not make sense to implement BFS recursively, as the call stack does not easily function as a queue.

This is a breadth first traversal of the BST from above:

```python
def BFS(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        print(node.value)
```
