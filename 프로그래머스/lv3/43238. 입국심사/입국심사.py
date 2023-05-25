def solution(n, times):
    start = 1  # 최소 시간
    end = max(times) * n  # 최대 시간

    answer = 0
    while start <= end:
        mid = (start + end) // 2  # 중간 시간

        count = 0  # mid 시간 동안 처리 가능한 사람 수
        for t in times:
            count += mid // t

        if count >= n:  # mid 시간 동안 처리 가능한 사람 수가 n보다 크거나 같으면
            answer = mid  # answer를 갱신하고
            end = mid - 1  # 더 적은 시간에서의 가능성을 확인하기 위해 end를 줄임
        else:
            start = mid + 1  # mid 시간 동안 처리 가능한 사람 수가 n보다 작으면 start를 늘림

    return answer
