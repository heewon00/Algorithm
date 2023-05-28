def solution(N, stages): #스테이지 수, 스테이지 번호
    answer = {}
    person = len(stages)
    
    #스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    for i in range(1, N+1):
        if person!=0:
            answer[i] = stages.count(i) / person
            person -= stages.count(i)
        else:
            answer[i] = 0
    
    return sorted(answer, key=lambda i: answer[i], reverse=True)