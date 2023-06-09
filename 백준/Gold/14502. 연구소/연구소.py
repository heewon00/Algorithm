from collections import deque
import copy

def bfs():
    queue=deque()
    tmp_graph = copy.deepcopy(graph)

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x,y=queue.popleft()

        for i,j in zip(dx,dy):
            nx,ny = x+i,y+j

            if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))

    global answer
    cnt = 0
    for i in range(n):
        cnt+= tmp_graph[i].count(0)
    answer = max(answer, cnt)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0



n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

answer=0
makewall(0)
print(answer)
