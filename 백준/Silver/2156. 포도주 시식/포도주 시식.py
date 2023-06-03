n = int(input())
lst=[0]
for i in range(n):
    lst.append(int(input()))

dp=[0, lst[1]]
if n>1:
    dp.append(lst[1]+lst[2])
for i in range(3, n+1):
    #i번째 제외, i-1번째 제외, i-2번째 제외
    dp.append(max(dp[i-1], lst[i]+dp[i-2], lst[i-1]+lst[i]+dp[i-3]))

print(dp[n])
