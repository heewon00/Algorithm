import sys
from collections import deque
input = sys.stdin.readline
INF=int(1e9)

n = int(input()) #도시의 개수
m = int(input()) #버스의 개수

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [0]*(n+1)


#출발 도시, 도착 도시, 버스 비용
for _ in range(m):
   s, e, f = map(int,input().split())
   graph[s].append((f, e))

start, end = map(int, input().split())

def dijkstra(start):
    queue = deque([(0, start)])
    distance[start] = 0

    while queue:
        nowfee, node = queue.popleft()

        if distance[node] < nowfee:
            continue

        for fee, end in graph[node]:
            cost = nowfee + fee
            if distance[end] > cost:
                distance[end] = cost
                queue.append((distance[end],end))
                
dijkstra(start)
print(distance[end])
            
    
