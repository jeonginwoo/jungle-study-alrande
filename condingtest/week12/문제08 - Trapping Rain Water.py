"""
출처 : Leet Code
번호 : 42
난이도 : Hard
제목 : Trapping Rain Water
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max-height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max-height[right]
        return result


# ==============================================
CaseCount = 2
case = []
case.append([0,1,0,2,1,0,1,3,2,1,2,1])
case.append([4,2,0,3,2,5])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("height:", case[i])
    print("result:", Solution().trap(case[i]))
