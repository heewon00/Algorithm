def solution(genres, plays):
    genre_dic=dict() #'장르' : [장르의 재생 횟수, [(음악 재생 횟수, 고유번호),...,]]
    
    for i in range(len(genres)):
        if genres[i] not in genre_dic:
            genre_dic[genres[i]] = [plays[i], [(plays[i],i)]]
        else:
            genre_dic[genres[i]][0] += plays[i]
            genre_dic[genres[i]][1].append((plays[i],i))
    
    sort_genre = sorted(list(genre_dic.values()), key=lambda x:-x[0])
    answer=[]
    for genre_cnt, info in sort_genre:
        info.sort(key=lambda x:(-x[0], x[1]))
        for song_cnt, idx in info[:2]:
            answer.append(idx)
        
    return answer