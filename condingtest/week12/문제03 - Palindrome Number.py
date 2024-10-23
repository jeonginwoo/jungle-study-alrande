"""
출처 : Leet Code
번호 : 15
난이도 : Medium
제목 : 3Sum
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if s == s[::-1]:
            return True
        return False



#############################################
case = {}
case[1] = [121]
case[2] = [-121]
case[3] = [10]
for i in range(1, 4):
    print(f"=== Case {i} ===")
    print("x:", case[i][0])
    print("result:", Solution().isPalindrome(case[i][0]))
    print()
