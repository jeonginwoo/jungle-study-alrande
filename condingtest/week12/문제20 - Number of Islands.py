"""
출처 : Leet Code
번호 : 200
난이도 : Medium
제목 : Number of Islands
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        start = []
        result = 0
        stack = []
        visited = [[False]*n for _ in range(m)]
        for start_x in range(m):
            for start_y in range(n):
                if grid[start_x][start_y] == "0" or visited[start_x][start_y]:
                    continue
                stack.append([start_x, start_y])
                visited[start_x][start_y] = True
                while stack:
                    now_x, now_y = stack.pop()
                    for i in range(4):
                        next_x = now_x+dx[i]
                        next_y = now_y+dy[i]
                        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            stack.append([next_x, next_y])
                            visited[next_x][next_y] = True
                result += 1
        return result


# ==============================================
CaseCount = 2
case = []
case.append([["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]])
case.append([["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("grid:", case[i])
    print("result:", Solution().numIslands(case[i]))
    print()
