n=int(input())
lst=sorted(list(map(int,input().split())),reverse=True)

print(sum(i*lst[i-1] for i in range(1,n+1)))
