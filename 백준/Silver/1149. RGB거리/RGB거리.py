'''
- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''
#DP

n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
for i in range(1, n):
    lst[i][0] = min(lst[i-1][1], lst[i-1][2]) + lst[i][0] #r
    lst[i][1] = min(lst[i-1][0], lst[i-1][2]) + lst[i][1] #g
    lst[i][2] = min(lst[i-1][0], lst[i-1][1]) + lst[i][2] #b
print(min(lst[n-1][0], lst[n-1][1], lst[n-1][2]))