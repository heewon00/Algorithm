import sys
import heapq

input = sys.stdin.readline

v,e = map(int, input().split()) #정점의 개수, 간선의 개수
k = int(input()) #시작 정점의 번호

graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF]*(v+1)

#u->v, w
for _ in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for w,v in graph[now]:
            cost = dist + w
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(k)

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
            
