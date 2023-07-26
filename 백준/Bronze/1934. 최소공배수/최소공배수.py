import sys

input = sys.stdin.readline

t = int(input())


def lcm(a,b):
    if a<b:
        a,b=b,a

    while a%b!=0:
        a,b=b,a%b

    return b


for _ in range(t):
    a,b=map(int,input().split())
    print(a * b // lcm(a,b))