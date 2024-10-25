"""
출처 : Leet Code
번호 : 15
난이도 : Medium
제목 : 3Sum
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum_lr = nums[left] + nums[right]
                if nums[i] + sum_lr < 0:
                    left += 1
                elif nums[i] + sum_lr > 0:
                    right -= 1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        result = list(map(list, {tuple(l) for l in result}))
        return result


#############################################
case = {}
case[1] = [[-1,0,1,2,-1,-4]]
case[2] = [[0,1,1]]
case[3] = [[0,0,0]]
for i in range(1, 4):
    print(f"=== Case {i} ===")
    print("nums:", case[i][0])
    print("result:", Solution().threeSum(case[i][0]))
    print()
