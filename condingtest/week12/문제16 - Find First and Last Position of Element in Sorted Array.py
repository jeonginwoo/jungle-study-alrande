"""
출처 : Leet Code
번호 : 34
난이도 : Medium
제목 : Find First and Last Position of Element in Sorted Array
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = last = -1
        i = 0
        while i<len(nums) and nums[i]!=target:
            i+=1
        if i<len(nums) and nums[i] == target:
            first = last = i
        while i<len(nums):
            if nums[i] == target:
                last = i
            i+=1
        return [first, last]



# ==============================================
CaseCount = 3
case = dict()
case[1] = [[5, 7, 7, 8, 8, 10], 8]
case[2] = [[5, 7, 7, 8, 8, 10], 6]
case[3] = [[], 0]
for i in range(1, CaseCount + 1):
    print(f"=== Case {i} ===")
    print("nums:", case[i][0])
    print("target:", case[i][1])
    print("result:", Solution().searchRange(case[i][0], case[i][1]))
    print()
