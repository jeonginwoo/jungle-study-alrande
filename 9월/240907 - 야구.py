"""
일시 : 24.09.07(토) 20:00
출처 : 백준
번호 : 32195
난이도 : 실버 1
제목 : 야구
시간 : 2시간 + 물어봄
"""

import sys
input = sys.stdin.readline

N = int(input())
foul = 0
arr_xy = []
for _ in range(N):
    x, y = map(int, input().split())
    if y>=-x and y>=x:
        arr_xy.append(x*x+y*y)
    else:
        foul+=1
arr_xy.sort()
Q = int(input())
arr_R = []
for _ in range(Q):
    R = int(input())
    arr_R.append(R*R)

for R in arr_R:
    result = [foul, 0, 0]
    left = 0
    right = len(arr_xy)-1
    while left <= right:
        mid = (left + right)//2
        if arr_xy[mid] <= R:
            left = mid+1
        else:
            right = mid-1
    result[1] += left
    result[2] += len(arr_xy)-left
    print(*result)