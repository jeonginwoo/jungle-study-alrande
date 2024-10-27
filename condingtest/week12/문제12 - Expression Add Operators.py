"""
출처 : Leet Code
번호 : 282
난이도 : Hard
제목 : Expression Add Operators
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def backtrack(index, expression, prev_operand, current_total):
            if index == len(num):
                if current_total == target:
                    result.append(expression)
                return
            
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break
                
                current_str = num[index:i+1]
                current_value = int(current_str)
                
                if index == 0:
                    backtrack(i + 1, current_str, current_value, current_value)
                else:
                    backtrack(i + 1, expression + "+" + current_str, current_value, current_total + current_value)
                    backtrack(i + 1, expression + "-" + current_str, -current_value, current_total - current_value)
                    backtrack(i + 1, expression + "*" + current_str, prev_operand * current_value, current_total - prev_operand + (prev_operand * current_value))

        result = []
        backtrack(0, "", 0, 0)
        return result
        

# ==============================================
CaseCount = 1
case = []
case.append(["105", 5])
case.append(["232", 8])
case.append(["123", 6])
case.append(["3456237490", 9191])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("num:", case[i][0])
    print("target:", case[i][1])
    print("result:", Solution().addOperators(case[i][0], case[i][1]))
