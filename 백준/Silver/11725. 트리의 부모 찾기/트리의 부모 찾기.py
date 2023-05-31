import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
parent = [0]*(n+1)      
graph=[ [] for _ in range(n+1) ]

for _ in range(n-1):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(start):
    for i in graph[start]: #start의 부모노드 찾기
        if parent[i] == 0: #아직 부모 노드 못 찾았다면
            parent[i] = start
            dfs(i)

dfs(1) #루트노드 1에서부터 시작
for i in range(2, n+1):
    print(parent[i])
