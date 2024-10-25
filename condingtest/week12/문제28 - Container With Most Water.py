"""
출처 : Leet Code
번호 : 11
난이도 : Medium
제목 : Container With Most Water
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_water = 0
        while left < right:
            now_water = (right-left)*min(height[left], height[right])
            max_water = max(max_water, now_water)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                temp_l = left + 1
                temp_r = right - 1
                while temp_l < temp_r:
                    if height[temp_l] > height[left]:
                        left = temp_l
                        break
                    elif height[temp_l] < height[left]:
                        right = temp_r
                        break
                    temp_l += 1
                    temp_r -= 1
                if left == temp_l-1 and right == temp_r+1:
                    break
        return max_water


# ==============================================
CaseCount = 2
case = []
case.append([1,8,6,2,5,4,8,3,7])
case.append([1,1])
for i in range(CaseCount):
    print()
    print(f"=== Case {i+1} ===")
    print("height:", case[i])
    print("result:", Solution().maxArea(case[i]))
