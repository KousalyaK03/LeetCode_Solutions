# Last updated: 7/10/2025, 5:46:00 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        processed_courses = 0

        while queue:
            current = queue.popleft()
            processed_courses += 1


            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return processed_courses == numCourses

"""
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
                
            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# Approach:
# 1. Represent the course prerequisites as a directed graph using an adjacency list.
# 2. Perform a topological sort using Kahn's algorithm (BFS) to detect cycles.
# 3. If all courses are processed (no cycle detected), return True; otherwise, return False.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list and in-degree count
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Count of courses that can be processed
        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1

            # Reduce the in-degree of dependent courses
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are processed, return True; otherwise, there's a cycle
        return processed_courses == numCourses

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E) for the adjacency list and in-degree array.

 """       
