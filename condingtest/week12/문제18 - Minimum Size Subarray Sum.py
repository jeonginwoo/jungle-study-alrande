"""
출처 : Leet Code
번호 : 209
난이도 : Medium
제목 : Minimum Size Subarray Sum
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = float("inf")
        left = right = 0
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                if curr_sum == target:
                    result = min(result, right-left+1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return result if result != float("inf") else 0


# ==============================================
CaseCount = 3
case = dict()
case[1] = [7, [2,3,1,2,4,3]]
case[2] = [4, [1,4,4]]
case[3] = [11, [1,1,1,1,1,1,1,1]]
for i in range(1, CaseCount + 1):
    print(f"=== Case {i} ===")
    print("target:", case[i][0])
    print("nums:", case[i][1])
    print("result:", Solution().minSubArrayLen(case[i][0], case[i][1]))
    print()
