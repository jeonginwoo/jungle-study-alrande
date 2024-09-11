"""
일시 : 24.09.07(토) 22: 26
출처 : 백준
번호 : 1193
난이도 : 실버 5
제목 : 파일 합치기 3
시간 : 22
"""

import sys
input = sys.stdin.readline

X = int(input())
count = 0
remain = X
while remain > 0:
    count += 1
    remain -= count
remain += count
if count % 2 == 0:
    print(f"{remain}/{count+1-remain}")
else:
    print(f"{count+1-remain}/{remain}")