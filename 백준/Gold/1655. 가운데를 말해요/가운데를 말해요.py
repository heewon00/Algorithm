import heapq
import sys

input = sys.stdin.readline

n=int(input())
left=[] 
right=[] 

for _ in range(n):
    i = int(input())

    #right힙으로 heappop했을 때
    if len(left)==len(right):
        heapq.heappush(left, -i)
    else:
        heapq.heappush(right, i)

    if right and right[0] < -left[0] :
        #자리 변경
        ltemp = heapq.heappop(left)
        rtemp = heapq.heappop(right)
        heapq.heappush(right, -ltemp)
        heapq.heappush(left, -rtemp)

    print(-left[0])
