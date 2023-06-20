import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    visited[x]=1
    cnt=0

    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=1
                queue.append(i)
                cnt+=1
    return cnt


input = sys.stdin.readline
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(n+1)
    print(bfs(1))
    
