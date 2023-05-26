def solution(numbers, target):
    answer=0
    n = len(numbers)
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == n:
            if total == target: #끝까지 다 돌았을때 합이 target이라면
                answer+=1
            return
        
        #아니라면
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0,0)
    return answer
        