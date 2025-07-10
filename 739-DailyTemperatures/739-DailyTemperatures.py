# Last updated: 7/10/2025, 3:51:26 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}  # to keep clone node- original node

        def dfs(current_node):  # goes to dfs(1)
            if current_node in visited:  # if the 1 above is already in visited then
                return visited[current_node]  # return that one from visited

            clone = Node(current_node.val)  # else clone the 1 val and 
            visited[current_node] = clone   # add it to visited

            for neighbor in current_node.neighbors:  # we go through all neighbors of current node
                clone.neighbors.append(dfs(neighbor))  # so new values will be added to dfs and that wil be called until its empty. 
            return clone
        return dfs(node)


"""

from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # Map original node -> cloned node

        # Initialize queue for BFS
        queue = deque([node])
        visited[node] = Node(node.val)  # Clone the root node

        while queue:
            current = queue.popleft()  # Pop from front of queue

            # Iterate over all neighbors of current node
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # Clone neighbor and put it into visited map
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)  # Add neighbor to queue for later processing

                # Link cloned current node to cloned neighbor
                visited[current].neighbors.append(visited[neighbor])

        # Return the clone of the starting node
        return visited[node]

# Explain your approach in brief:
# This approach uses a DFS traversal to clone the graph. 
# A hash map is used to store already cloned nodes to avoid redundant work and infinite recursion.

# Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
# Space Complexity: O(N), for storing visited nodes in the hash map and the recursion stack.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to store cloned nodes
        cloned_nodes = {}

        def dfs(current: Node) -> Node:
            # If the node is already cloned, return it
            if current in cloned_nodes:
                return cloned_nodes[current]

            # Clone the current node
            cloned_node = Node(current.val)
            cloned_nodes[current] = cloned_node

            # Recursively clone all neighbors
            for neighbor in current.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node

        # If the input node is None, return None
        if not node:
            return None
        
        # Start DFS from the given node
        return dfs(node)


"""
