"""
일시 : 24.09.12(목) 16:54
출처 : 백준
번호 : 11652
난이도 : 실버 4
제목 : 카드
시간 : 13분
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
d = defaultdict(int)
for _ in range(N):
    d[int(input())] += 1
arr = list(d.keys())
arr.sort()
max_count = 0
card = 0
for i in range(len(arr)):
    if max_count < d[arr[i]]:
        max_count = d[arr[i]]
        card = arr[i]
print(card)