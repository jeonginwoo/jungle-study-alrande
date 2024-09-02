"""
일시 : 24.09.02(월) 14:15
출처 : 백준
번호 : 30089
난이도 : 실버 3
제목 : 2×n 타일링
시간 : 30분
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [0]
count = 0
for i in range(N//2+1):
    a = 1
    b = 1
    for j in range(N-i, N-i*2, -1):
        a *= j
    for k in range(i, 0, -1):
        b *= k
    count += a//b
print(count%10007)