"""
출처 : Leet Code
번호 : 70
난이도 : Easy
제목 : Climbing Stairs
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for k in range(2, n+1):
            dp[k] = dp[k-1] + dp[k-2]
        return dp[n]


# ==============================================
CaseCount = 2
case = []
case.append(2)
case.append(3)
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("n:", case[i])
    print("result:", Solution().climbStairs(case[i]))
    print()
