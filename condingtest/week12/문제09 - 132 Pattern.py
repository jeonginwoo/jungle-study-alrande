"""
출처 : Leet Code
번호 : 456
난이도 : Medium
제목 : 132 Pattern
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_arr = [nums[0]]
        for i in range(1, len(nums)):
            min_arr.append(min(nums[i], min_arr[-1]))

        stack = []
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > min_arr[i]:
                while stack and stack[-1] <= min_arr[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])

        return False


# ==============================================
CaseCount = 3
case = []
case.append([1,2,3,4])
case.append([3,1,4,2])
case.append([-1,3,2,0])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("nums:", case[i])
    print("result:", Solution().find132pattern(case[i]))
