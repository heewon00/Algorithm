t=int(input())
for _ in range(t):
    lst = list(input())
    sum=0
    for i in lst:
        if i=='(':
            sum+=1
        else:
            sum-=1
        if sum<0:
            print("NO")
            break
    if sum>0:
        print("NO")
    elif sum==0:
        print("YES")