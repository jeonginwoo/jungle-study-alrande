"""
일시 : 24.09.03(화) 12:30
출처 : 백준
번호 : 5545
난이도 : 실버 3
제목 : 최고의 피자
시간 : 20분
"""

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)] + [0]
D.sort(reverse=True)
result = 0
D_sum = 0
for k in range(N+1):
    D_sum += D[k-1]
    result = max(result, (C + D_sum)//(A+B*k))
print(result)