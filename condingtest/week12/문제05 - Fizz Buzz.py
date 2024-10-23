"""
출처 : Leet Code
번호 : 7
난이도 : Medium
제목 : Reverse Integer
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for num in range(1, n+1):
            add = ""
            if num % 3 == 0:
                add += "Fizz"
            if num % 5 == 0:
                add += "Buzz"
            if num % 3 != 0 and num % 5 != 0:
                add += str(num)
            result.append(add)
        return result


#############################################
case = {}
case[1] = [3]
case[2] = [5]
case[3] = [15]
for i in range(1, 4):
    print(f"=== Case {i} ===")
    print("x:", case[i][0])
    print("result:", Solution().fizzBuzz(case[i][0]))
    print()
