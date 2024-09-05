"""
일시 : 24.09.05(수) 18:20
출처 : 백준
번호 : 7983
난이도 : 골드 5
제목 : 내일 할거야
시간 : 25분
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: -x[1])
arr.append([0, 0])

result = 0
for i in range(n):
    d1, t1 = arr[i]
    d2, t2 = arr[i+1]
    if i == n-1:
        result = max(result, t1-d1-t2)
    if t1-d1 < t2:
        arr[i+1][1] = t1-d1

print(result)
