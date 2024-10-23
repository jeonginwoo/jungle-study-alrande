"""
출처 : Leet Code
번호 : 7
난이도 : Medium
제목 : Reverse Integer
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = None
        if x < 0:
            x = -x
            result = -int(str(x)[::-1])
        else:
            result = int(str(x)[::-1])
        return result if -2**31 <= result <= 2**31-1 else 0



#############################################
case = {}
case[1] = [123]
case[2] = [-123]
case[3] = [120]
for i in range(1, 4):
    print(f"=== Case {i} ===")
    print("x:", case[i][0])
    print("result:", Solution().reverse(case[i][0]))
    print()
