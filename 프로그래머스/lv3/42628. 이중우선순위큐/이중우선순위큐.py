import heapq
def solution(operations):
    answer = []
    
    for i in operations:
        command, num = i.split()

        if command=='I':
            heapq.heappush(answer,int(num))
        else: #D
            if not answer:
                continue
            if num=='-1': #최소
                heapq.heappop(answer)
            else: #최대
                answer.remove(max(answer))
                heapq.heapify(answer)
        print(answer)
    if not answer:
        return [0,0]
    else:
        return [max(answer),answer[0]]