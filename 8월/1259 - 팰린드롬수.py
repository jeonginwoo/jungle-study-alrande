"""
일시 : 24.08.31(금) 12:35
출처 : 백준
번호 : 1259
난이도 : 브론즈 1
제목 : 팰린드롬수
"""

import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == "0":
        break

    is_p = True

    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            is_p = False
            break

    print("yes" if is_p else "no")
