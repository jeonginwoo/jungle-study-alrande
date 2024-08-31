"""
일시 : 24.08.30(금) 12:30
출처 : 백준
번호 : 1780
난이도 : 실버 2
제목 : 종이의 개수
"""

import sys
input = sys.stdin.readline

def func(n, x, y):
    global count
    num = arr[x][y]
    if n == 1:
        result[num] += 1
        return

    check = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                check = False
                break
        if not check:
            break

    if check:
        result[num] += 1
    else:
        new_n = n//3
        for i in range(3):
            for j in range(3):
                func(new_n, x+new_n*i, y+new_n*j)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0
result = [0, 0, 0]
func(N, 0, 0)
print(result[-1], result[0], result[1], sep="\n")