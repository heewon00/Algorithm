import math
def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())

    a, b = n//2, n//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1