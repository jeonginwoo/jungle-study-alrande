"""
일시 : 24.09.04(수) 22:20
출처 : 백준
번호 : 18126
난이도 : 실버 2
제목 : 너구리 구구
시간 : 15분
"""

import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])

stack = [1]
visited = [False]*(N+1)
visited[1] = True
distance = [0]*(N+1)
while stack:
    now = stack.pop()
    for next, weight in edges[now]:
        if not visited[next]:
            stack.append(next)
            visited[next] = True
            distance[next] = distance[now] + weight
print(max(distance))
