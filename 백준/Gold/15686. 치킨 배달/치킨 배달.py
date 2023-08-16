import sys
from itertools import combinations as com
input = sys.stdin.readline

#치킨거리 = 집에서 가장 가까운 치킨집의 거리 : abs(r1-r2) + abs(c1-c2)
#도시의 치킨 거리는 모든 집의 치킨 거리의 합
#0 빈칸, 1 집, 2 치킨집

n,m=map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9

#집과 치킨집의 좌표 저장
house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i,j))
        elif graph[i][j]==2:
            chicken.append((i,j))

#m개의 치킨집 좌표 고르기
for c in com(chicken, m):
    #모든 집에 대해 치킨거리 계산
    temp = 0
    for hx,hy in house:
        mini = 1e9
        #한 집에 대해 어느 치킨집이 가장 가까운지 계산
        for cx,cy in c:
            mini = min(mini, abs(hx-cx)+abs(hy-cy))
        temp+=mini
    answer = min(temp, answer)
print(answer)
        
