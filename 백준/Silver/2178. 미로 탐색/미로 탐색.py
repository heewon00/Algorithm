import sys
from collections import deque

input = sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i,j in zip(dx,dy):
            nx,ny=x+i,y+j

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[-1][-1]




print(bfs(0,0))
    
