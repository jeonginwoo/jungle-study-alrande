"""
출처 : Leet Code
번호 : 52
난이도 : Hard
제목 : N-Queens II
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find(x, line1, line2, line3):
            count = 0
            for y in range(n):
                if not (line1[y] or line2[y + x] or line3[y - x + n]):
                    if x == n - 1:
                        count += 1
                    else:
                        line1[y] = line2[y + x] = line3[y - x + n] = True
                        count += find(x + 1, line1, line2, line3)
                        line1[y] = line2[y + x] = line3[y - x + n] = False
            return count

        line1 = [False] * n
        line2 = [False] * (2 * n + 1)
        line3 = [False] * (2 * n + 1)
        return find(0, line1, line2, line3)




# ==============================================
CaseCount = 2
case = []
case.append(4)
case.append(1)
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("n:", case[i])
    print("result:", Solution().totalNQueens(case[i]))
    print()
