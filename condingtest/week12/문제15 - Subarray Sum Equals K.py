"""
출처 : Leet Code
번호 : 560
난이도 : Medium
제목 : Subarray Sum Equals K
"""

from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        prefix_sum = 0
        prefix_array = {0:1}

        for num in nums:
            prefix_sum += num
            if prefix_sum-k in prefix_array:
                result = result + prefix_array[prefix_sum-k]

            if prefix_sum in prefix_array:
                prefix_array[prefix_sum] += 1
            else:
                prefix_array[prefix_sum] = 1
        return result


    #==============================================
CaseCount = 3
case = []
case.append([[1,-1,0], 0])
case.append([[1,1,1], 2])
case.append([[1,2,3], 3])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("nums:", case[i][0])
    print("k:", case[i][1])
    print("result:", Solution().subarraySum(case[i][0], case[i][1]))
    print()
