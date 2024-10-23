"""
출처 : Leet Code
번호 : 22
난이도 : Medium
제목 : Generate Parentheses
"""

class Solution(object):
    def __init__(self):
        self.results = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.func([], n, "")
        return self.results

    def func(self, stack, n, result):
        if n == 0:
            for i in range(len(stack)):
                result+=")"
            self.results.append(result)
            return

        temp = stack[:]
        temp.append("(")
        self.func(temp, n-1, result+"(")
        if len(stack) > 0:
            self.func(stack[:-1], n, result+")")



#############################################
CaseCount = 2
case = dict()
case[1] = [3]
case[2] = [1]
for i in range(1, CaseCount+1):
    print(f"=== Case {i} ===")
    print("x:", case[i][0])
    print("result:", Solution().generateParenthesis(case[i][0]))
    print()
