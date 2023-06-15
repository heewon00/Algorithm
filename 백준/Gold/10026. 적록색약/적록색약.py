'''
적록색약 : R==G
'''

import sys
from collections import deque

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def bfs(x, y):
    queue.append((x,y))
    visited[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x, y = queue.popleft()

        for i,j in zip(dx,dy):
            nx = x + i ; ny = y + j
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))

n=int(input())
graph=[list(input()) for _ in range(n)]
queue = deque()

#적록색약x
visited = [[0]*n for _ in range(n)]
case1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            case1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

#적록색약o
visited = [[0]*n for _ in range(n)]
case2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            case2 += 1

print(case1, case2)
