"""
일시 : 24.09.01(금) 21:05
출처 : 백준
번호 : 30089
난이도 : 실버 4
제목 : 새로운 문자열 만들기
시간 : 10분
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().strip()
    reverse = string[::-1]
    result = ""
    for i in range(len(string)):
        if string[i:] == reverse[:len(string)-i]:
            result = string[:i] + string[i:] + reverse[len(string)-i:]
            break
    print(result)