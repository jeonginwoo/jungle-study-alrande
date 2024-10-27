"""
출처 : Leet Code
번호 : 218
난이도 : Hard
제목 : The Skyline Problem
"""

import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for left, right, height in buildings:
            events.append([left, -height])
            events.append([right, height])
        events.sort()

        result = []
        max_heap = [0]
        prev_max_height = 0
        for point, height in events:
            if height < 0:
                heapq.heappush(max_heap, height)
            else:
                max_heap.remove(-height)
                heapq.heapify(max_heap)

            curr_max_height = -max_heap[0]
            if curr_max_height != prev_max_height:
                result.append([point, curr_max_height])
                prev_max_height = curr_max_height

        return result



# ==============================================
CaseCount = 2
case = []
case.append([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
case.append([[0,2,3],[2,5,3]])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("buildings:", case[i])
    print("result:", Solution().getSkyline(case[i]))
