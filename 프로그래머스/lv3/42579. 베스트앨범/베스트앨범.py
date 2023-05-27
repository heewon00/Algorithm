def solution(genres, plays):
    playlist=[] #정렬
    genre_dic=dict() #총 재생 횟수
    
    for i in range(len(genres)):
        if genres[i] not in genre_dic:
            genre_dic[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]] += plays[i]
        playlist.append((genres[i],plays[i],i))
    
    genre_dic = sorted(genre_dic.items(), key=lambda x:-x[1])
    playlist.sort(key=lambda x:(-x[1], x[2]))
    
    result_dic=dict()
    for genre, play in genre_dic:
        result_dic[genre] = []
        
    for g,p,i in playlist:
        result_dic[g].append(i)
    
    answer = sum([i[:2] for i in result_dic.values()],[])
    
    return answer