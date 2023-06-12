'''
R 뒤집기
D 첫 번째 수 버리기(비어있으면 error)
'''
import sys
from collections import deque
input = sys.stdin.readline
T=int(input())

for i in range(T):
    rev=0 #R이 짝수인지 홀수인지 계산하는데 쓰임
    p=input().rstrip() #수행할 함수
    n=int(input()) #배열 수
    flag = input().rstrip()[1:-1]
    if flag=='':
        lst = deque([])
    else:
        lst = deque(flag.split(","))

    for func in p:
        if func=="R":
            rev+=1
        else:
            if lst:
                if rev%2==0:
                    lst.popleft() 
                else:
                    lst.pop()
            else:
                print('error')
                break
    else:
        if rev%2!=0:
            lst.reverse()
        print('['+','.join(lst)+']')
