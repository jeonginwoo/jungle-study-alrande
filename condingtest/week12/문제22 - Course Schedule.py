"""
출처 : Leet Code
번호 : 207
난이도 : Medium
제목 : Course Schedule
"""

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prev_to_next = [[] for _ in range(numCourses)]
        next_to_prev = [[] for _ in range(numCourses)]
        start_courses = set([x for x in range(numCourses)])
        for prev, next in prerequisites:
            prev_to_next[prev].append(next)
            next_to_prev[next].append(prev)
            if next in start_courses:
                start_courses.remove(next)

        while start_courses:
            now = start_courses.pop()
            numCourses -= 1
            for next in prev_to_next[now]:
                next_to_prev[next].remove(now)
                if len(next_to_prev[next]) == 0:
                    start_courses.add(next)

        return numCourses == 0



# ==============================================
CaseCount = 6
case = []
case.append([2, [[1,0]]])
case.append([2, [[1,0],[0,1]]])
case.append([5, [[1,4],[2,4],[3,1],[3,2]]])
case.append([1, []])
case.append([20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]])
case.append([3, [[1,0],[2,0]]])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("numCourses:", case[i][0])
    print("prerequisites:", case[i][1])
    print("result:", Solution().canFinish(case[i][0], case[i][1]))
    print()
