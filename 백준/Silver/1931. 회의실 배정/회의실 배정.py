import sys
input = sys.stdin.readline

#빨리 끝나는 회의 -> 일찍 시작하는 회의 순

n=int(input())
meeting = [list(map(int,input().split())) for _ in range(n)]
meeting.sort(key=lambda x:(x[1],x[0]))

cnt=1
flag=meeting[0][1]
#i번째 회의의 시작 시간이 이전 회의의 끝나는 시간보다 같거나 크면 cnt+=1
for i in range(1,n):
    if flag <= meeting[i][0]:
        cnt+=1
        flag=meeting[i][1]
        
print(cnt)
