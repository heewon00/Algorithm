import sys
input = sys.stdin.readline

N = int(input())
Nlst = set(map(int, input().split()))
M = int(input())
Mlst = list(map(int, input().split()))

for x in Mlst:		
    print(1) if x in Nlst else print(0)