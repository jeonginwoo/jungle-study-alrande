"""
출처 : Leet Code
번호 : 5
난이도 : Medium
제목 : Longest Palindromic Substring
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False]*len(s) for _ in range(len(s))]
        max_len = 0
        max_pal = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                left = j-i
                right = j
                if s[left] == s[right]:
                    if i == 0 or i == 1 or dp[left+1][right-1]:
                        dp[left][right] = True
                        if max_len < right-left+1:
                            max_len = right-left+1
                            max_pal = s[left:right+1]
        return max_pal


# ==============================================
CaseCount = 2
case = []
case.append("babad")
case.append("cbbd")
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("s:", case[i])
    print("result:", Solution().longestPalindrome(case[i]))
    print()
