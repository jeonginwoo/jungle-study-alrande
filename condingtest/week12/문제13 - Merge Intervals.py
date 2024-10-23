"""
출처 : Leet Code
번호 : 56
난이도 : Medium
제목 : Merge Intervals
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                merge = result.pop()
                merge = [merge[0], max(merge[1], intervals[i][1])]
                result.append(merge)
            else:
                result.append(intervals[i])
        return result


#############################################
CaseCount = 2
case = dict()
case[1] = [[1,3],[2,6],[8,10],[15,18]]
case[2] = [[1,4],[4,5]]
for i in range(1, CaseCount+1):
    print(f"=== Case {i} ===")
    print("x:", case[i])
    print("result:", Solution().merge(case[i]))
    print()
