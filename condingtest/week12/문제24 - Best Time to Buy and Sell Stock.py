"""
출처 : Leet Code
번호 : 121
난이도 : Easy
제목 : Best Time to Buy and Sell Stock
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        max_price = 0
        for i in range(len(prices)-1, 0, -1):
            max_price = max(max_price, prices[i])
            result = max(result, max_price-prices[i-1])
        return result



# ==============================================
CaseCount = 2
case = []
case.append([7,1,5,3,6,4])
case.append([7,6,4,3,1])
for i in range(CaseCount):
    print(f"=== Case {i+1} ===")
    print("prices:", case[i])
    print("result:", Solution().maxProfit(case[i]))
    print()
