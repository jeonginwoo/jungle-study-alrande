"""
출처 : Leet Code
번호 : 20
난이도 : Easy
제목 : Valid Parenthesis
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mate = dict()
        mate["("] = ")"
        mate["["] = "]"
        mate["{"] = "}"
        stack = []
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else:
                if len(stack) > 0 and mate[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False


#############################################
CaseNum = 4
case = {}
case[1] = ["()"]
case[2] = ["()[]{}"]
case[3] = ["(]"]
case[4] = ["([])"]
for i in range(1, CaseNum+1):
    print(f"=== Case {i} ===")
    print("s:", case[i][0])
    print("result:", Solution().isValid(case[i][0]))
    print()
