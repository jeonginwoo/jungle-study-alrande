"""
출처 : Leet Code
번호 : 300
난이도 : Medium
제목 : Longest Increasing Subsequence
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            temp = [dp[x] for x in range(i) if nums[x] < nums[i]]+[0]
            dp[i] = max(temp) + 1
        return max(dp)


# ==============================================
CaseCount = 3
case = []
case.append([10,9,2,5,3,7,101,18])
case.append([0,1,0,3,2,3])
case.append([7,7,7,7,7,7,7])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("nums:", case[i])
    print("result:", Solution().lengthOfLIS(case[i]))
    print()
