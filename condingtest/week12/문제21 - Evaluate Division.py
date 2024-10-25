"""
출처 : Leet Code
번호 : 399
난이도 : Medium
제목 : Evaluate Division
"""
from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(now, value, query, edges, visited):
            if now == query[1]:
                return value
            visited.add(now)
            for next_node, weight in edges[now]:
                if next_node not in visited:
                    result = dfs(next_node, value * weight, query, edges, visited)
                    if result != -1:
                        return result
            return -1

        edges = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            edges[a].append((b, values[i]))
            edges[b].append((a, 1 / values[i]))

        result = []
        for query in queries:
            if query[0] not in edges or query[1] not in edges:
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1.0)
            else:
                visited = set()
                res = dfs(query[0], 1, query, edges, visited)
                result.append(res if res != -1 else -1.0)

        return result


# ==============================================
CaseCount = 3
case = []
case.append([[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]])
case.append([[["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]])
case.append([[["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("equations:", case[i][0])
    print("values:", case[i][1])
    print("queries:", case[i][2])
    print("result:", Solution().calcEquation(case[i][0], case[i][1], case[i][2]))
    print()
