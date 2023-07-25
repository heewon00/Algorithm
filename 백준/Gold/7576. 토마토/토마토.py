import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))

while queue:
    x, y = queue.popleft()
    
    for i, j in zip(dx,dy):
        nx, ny = x+i, y+j

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))

ans = 0
for i in graph:
    if 0 in i:
        print(-1)
        break
    ans = max(ans, max(i))
else:
    print(ans - 1)

