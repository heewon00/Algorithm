def dfs(graph, visited, node):
    visited[node] = True  # 현재 노드를 방문 처리

    # 현재 노드와 연결된 모든 노드를 순회
    for i in range(len(graph)):
        if graph[node][i] == 1 and not visited[i]:  # 연결되어 있고 방문하지 않은 노드라면
            dfs(graph, visited, i)  # 해당 노드로 DFS 수행

def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부를 저장하는 배열

    # 모든 노드를 순회하면서 DFS 수행
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 노드라면
            dfs(computers, visited, i)  # DFS 수행
            answer += 1  # 연결 요소 개수 증가

    return answer
