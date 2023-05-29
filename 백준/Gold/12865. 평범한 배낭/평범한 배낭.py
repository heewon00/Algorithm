#물건 가치의 최댓값 출력
#knapsack
n, k = map(int,input().split()) #물건개수, 배냥 허용 무게
wvlst = [[0,0]] #w,v 기록
dp = [[0]*(k+1) for _ in range(n+1)] 

for i in range(n):
    #물건무게,가치
    wvlst.append(list(map(int, input().split())))

for i in range(1, n+1): #물건 개수
    for j in range(1, k+1): #배낭 허용 무게
        w = wvlst[i][0] #무게
        v = wvlst[i][1] #가치

        if j < w : #담으려는 물건이 허용 무게보다 크다면 넣지 않음
            dp[i][j] = dp[i-1][j]
        else:
            #현재 넣을 물건의 무게만큼 배낭에서 빼고 넣거나
            #현재 물건을 넣지 않는다
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
            #j-w일 때의 최대가치가 저장되어 있음

print(dp[n][k])

        
      