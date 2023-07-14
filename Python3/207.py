# Course Schedule

# This solution transforms the prerequisites into a graph represented as an adjacency list,
# then performs a topological traversal (see Kahn's algorithm) (note this is like BFS).
# Any node in a cycle can not be visited during a topological traversal because
# they will always have an incoming edge from the previous node in the cycle.
# Because of this, we know that there is a cycle in the course graph
# if the topological traversal does not visit every course.
class Solution0: # O(E+V) time, O(E+V) space (numPrereqs has a num for each course, adjacencyList contains every edge)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The numPrereqs list is used to see which nodes have 0 incoming edges
        # for the topological traversal, since the adjacency list stores outgoing
        # edges, not incoming.
        numPrereqs = [0]*numCourses # O(V) I guess? LC says so
        adjacencyList = [[] for _ in range(numCourses)]
        # Note that we have to use list comprehension and not the same technique as numPrereqs,
        # since that would shallow copy and create references to the same object

        for course, req in prerequisites: # O(E)
            numPrereqs[course] += 1
            adjacencyList[req].append(course) 
            # Note that the adjacency list contains a list of every course that the course corresponding
            # to the index is a prerequisite FOR.
            # This makes sense with the natural flow of the graph, as each course points to the courses
            # that you can now take after said course. 
            # In the topological traversal, this property allows the courses to be added to the queue
            # in the order they can be taken.

        topoQ = deque()
        for course, prereqs in enumerate(numPrereqs):
            if prereqs == 0: topoQ.append(course)

        nodesVisited = 0
        while topoQ: # O(V)
            node = topoQ.popleft()
            nodesVisited += 1
            for neighbor in adjacencyList[node]: # Iterate through courses that had node as a prereq (all edges, O(E) total)
                numPrereqs[neighbor] -= 1
                if numPrereqs[neighbor] == 0: # If you've completed all prereqs
                    topoQ.append(neighbor)
                
        return nodesVisited == numCourses


# This solution uses dfs to traverse the courses while tracking if a cycle occurs.
# This is done by checking if there is an edge from any node to one of its ancestors.
# We keep track of ancestors using a list inStack, where each value is a boolean
# that represents if the node corresponding to the index is an ancestor of the node being visited.
# Don't confuse this with the visit list, which is just to keep track of nodes that have been
# visited in general, which may not necessarily be an ancestor of the current node.
# You may be thinking, in an individual subgraph going through DFS, if a node reaches an already-
# visited node, it must be an ancestor.
# This is true, but we still need visit and inStack, since visit is important to keep track 
# BETWEEN iterations of dfs (in the loop at line 83) rather than inside a DFS iteration.
# Essentially, the visit list allows the the canFinish loop to skip over courses until it reaches a new subgraph.
class Solution1: # O(E+V) time and space
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The dfsHelper function performs dfs on the input node, and returns True if 
        # the subgraph containing node has a cycle
        def dfsHelper(node: int) -> bool:
            if inStack[node]: # If the node is already in the stack, we have a cycle. 
                return True
            if visit[node]:
                return False

            # Mark the current node as visited and part of current recursion stack.
            visit[node] = True
            inStack[node] = True

            # Iterate through each edge, O(E)
            for neighbor in adjList[node]: # Recursively dfs neighbors
                if dfsHelper(neighbor): # If a neighbor has a cycle
                    return True

            inStack[node] = False # Remove the node from the dfs call stack now that its children have been visited
            return False # There is no cycle, so return False

        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites: # O(E)
            adjList[prereq].append(course)

        visit = [False] * numCourses # O(V)
        inStack = [False] * numCourses
        # We need to perform dfs on every node because we don't know that the graph is connected;
        # We have to call dfsHelper for every course to ensure that we check them all
        for course in range(numCourses):
            if dfsHelper(course): # Iterates over every node once (thanks to visit[]), O(V)
                return False
        return True
        # Note that dfsHelper returns True if the node is in a subgraph with a cycle;
        # canFinish on the other hand returns False if there is a cycle, which is why the booleans here
        # are flipped compared to the similar for loop in dfsHelper.
        # This repetition is necessary because canFinish is looking for a cycle in all of the courses,
        # whereas dfsHelper is only looking for a cycle in the subgraph connected to the input node.

# Note that although S1 seems to lend itself better to iterative dfs, doing iterative dfs is difficult when
# the recursive call is not a tail call, since we need to access the each course when it is first visited,
# and after all of it's children have been visited. This means you have to explicitly iterate a call stack,
# since the typical iterative dfs implementation removes the parent node from the stack before visiting its children