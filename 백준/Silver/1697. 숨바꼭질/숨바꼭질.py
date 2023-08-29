from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
visited = [0]*100001
#걸으면 x-1, x+1
#순간이동하면 2*x

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()

        if x == k:
            print(visited[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0<=nx<100001 and not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x]+1

bfs()
