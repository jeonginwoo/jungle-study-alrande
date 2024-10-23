"""
출처 : Leet Code
번호 : 1
난이도 : Easy
제목 : Two Sum
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

case = {}
case[1] = [[2,7,11,15], 9]
case[2] = [[3,2,4], 6]
case[3] = [[3,3], 6]
for i in range(1, 4):
    print(f"=== Case {i} ===")
    print("nums:", case[i][0])
    print("target:", case[i][1])
    print("result:", Solution().twoSum(case[i][0], case[i][1]))
    print()
