import sys

n=int(input())
lst=[]
total=0
for _ in range(n):
    i=int(sys.stdin.readline())
    total+=i
    lst.append(i)

lst.sort()

print(round(total/n))
print(lst[n//2])

from collections import Counter
c = Counter(lst).most_common(2)
if n == 1:
    print(lst[0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
print(lst[-1] - lst[0])
