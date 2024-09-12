"""
일시 : 24.09.12(목) 19:50
출처 : 백준
번호 : 26215
난이도 : 실버 3
제목 : 눈 치우기
시간 : 30분
"""

import sys
input = sys.stdin.readline

N = int(input())
amount = list(map(int, input().split()))
result = max(max(amount), (sum(amount)+1) // 2)
print(result if result <= 1440 else -1)