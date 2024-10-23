"""
출처 : Leet Code
번호 : 3
난이도 : Medium
제목 : Longest Substring Without Repeating Characters
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 1
        max_len = 0
        while right <= len(s):
            substr = s[left:right]
            if right < len(s) and s[right] in substr:
                while left < right and s[left] != s[right]:
                    left += 1
                while left < right and s[left] == s[right]:
                    left += 1
            max_len = max(max_len, len(substr))
            right += 1
        return max_len



#==============================================
CaseCount = 3
case = dict()
case[1] = "abcabcbb"
case[2] = "bbbbb"
case[3] = "pwwkew"
for i in range(1, CaseCount+1):
    print(f"=== Case {i} ===")
    print("s:", case[i])
    print("result:", Solution().lengthOfLongestSubstring(case[i]))
    print()
