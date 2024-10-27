"""
출처 : Leet Code
번호 : 486
난이도 : Medium
제목 : Predict the Winner
"""


class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def play(left, right, turn):
            if left > right:
                return 0
            if turn == 0:
                return max(play(left+1, right, 1-turn) + nums[left],
                           play(left, right-1, 1-turn) + nums[right])
            else:
                return min(play(left+1, right, 1-turn) - nums[left],
                           play(left, right-1, 1-turn) - nums[right])
        return play(0, len(nums)-1, 0) >= 0


# ==============================================
CaseCount = 2
case = []
case.append([1,5,2])
case.append([1,5,233,7])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("nums:", case[i])
    print("result:", Solution().predictTheWinner(case[i]))
