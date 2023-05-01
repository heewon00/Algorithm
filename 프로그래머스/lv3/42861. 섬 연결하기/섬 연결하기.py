def solution(n, costs):
    answer = 0
    
    # [a, b, c] -> [연결할 섬 a, 연결할 섬 b, 건설 비용]
    # 건설 비용이 적은 것부터 섬을 연결할 것임
    # 건설 비용을 기준으로 오름차순 sort
    costs.sort(key = lambda x:x[2])
    
    # 초기 설정의 부모노드는 자기 자신임
    parent = [i for i in range(n)]
    
    # x의 부모 노드를 찾는 함수
    def find_parent(parent, x):
        #부모 노드가 자기 자신이 아니라면 자기 자신이 될 때까지 반복
        if parent[x]!=x: 
            # parent[x]의 부모 노드를 찾음
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b):
        #a, b의 부모노드를 각각 찾아서 숫자가 더 작은 것이 부모 노드가 됨
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a > b :
            parent[a] = b
        else:
            parent[b] = a
    
    for x, y, cost in costs:
        #아직 두 노드가 연결되지 않았다면
        if find_parent(parent, x) != find_parent(parent, y):
            answer += cost
            union_parent(parent, x, y) #두 노드 연결시켜줌
            
    return answer