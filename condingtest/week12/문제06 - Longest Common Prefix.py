"""
출처 : Leet Code
번호 : 14
난이도 : Easy
제목 : Longest Common Prefix
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        min_len = min(len(s) for s in strs)
        first = strs[0]
        for i in range(min_len):
            for j in range(1, len(strs)):
                if first[i] != strs[j][i]:
                    return result
            result+=first[i]
        return result


#############################################
CaseNum = 3
case = {}
case[1] = [["flower","flow","flight"]]
case[2] = [["dog","racecar","car"]]
case[3] = [["ab", "a"]]
for i in range(1, CaseNum+1):
    print(f"=== Case {i} ===")
    print("x:", case[i][0])
    print("result:", Solution().longestCommonPrefix(case[i][0]))
    print()
