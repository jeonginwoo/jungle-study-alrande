"""
출처 : Leet Code
번호 : 215
난이도 : Medium
제목 : Kth Largest Element in an Array
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        result = None
        for i in range(k):
            result = -heapq.heappop(maxHeap)
        return result


# ==============================================
CaseCount = 2
case = dict()
case[1] = [[3,2,1,5,6,4], 2]
case[2] = [[3,2,3,1,2,4,5,5,6], 4]
for i in range(1, CaseCount + 1):
    print(f"=== Case {i} ===")
    print("nums:", case[i][0])
    print("k:", case[i][1])
    print("result:", Solution().findKthLargest(case[i][0], case[i][1]))
    print()
