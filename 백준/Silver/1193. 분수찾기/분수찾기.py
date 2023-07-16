import sys
input = sys.stdin.readline

n = int(input())

#몇 번째 대각선인지
line = 1

while n > line:
    n -= line
    line += 1

# n이 짝수인 경우
if line % 2 == 0:
    up = n
    down = line - n + 1

# n이 홀수인 경
else:
    up = line - n + 1
    down = n

print(up,'/',down, sep="")