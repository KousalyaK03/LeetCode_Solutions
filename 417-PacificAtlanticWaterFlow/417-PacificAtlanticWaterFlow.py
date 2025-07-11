# Last updated: 7/11/2025, 4:23:45 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:  # there is no grid return empty
            return []
        # to get no. of rows, cols in the grid
        rows = len(heights)
        cols = len(heights[0])
        # to store unreapeated values for each of the oceans
        pacific, atlantic = set(), set()
        # this is for going to neighbors up, left, down, right
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(r, c, visited):
# we'll just add current cell as visited so that we won't have to visit it again
            visited.add((r,c))  
# we are going in all the directions for the neighbors
            for dr, dc in directions:
                nr,nc = r + dr, c + dc  # getting the neighbor cell

                if(
                    0 <= nr < rows and  # inbounds for rows 
                    0<= nc < cols and  # inbounds for cols 
                    (nr, nc) not in visited and  # must not be visited yet.
# neighbor heights must be >=. because we are going to reverse of the waterflow for this problem
                    heights[nr][nc] >= heights[r][c]):
                    # continue dfs for the neighbors
                    dfs(nr, nc, visited)
# start dfs for all pacific border cells
        for c in range(cols):
            dfs(0, c, pacific)  # top row pacific
            dfs(rows - 1, c, atlantic)  # bottom row atlantic
# start dfs for all atlantic border cells
        for r in range(rows):
            dfs(r, 0, pacific)  # left column pacific
            dfs(r, cols - 1, atlantic)  # right column atlantic
        result = []

        for r in range(rows):
            for c in range(cols):
# getting common cells from both oceans and appending them to list and returning them as result
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r,c])
        return result
