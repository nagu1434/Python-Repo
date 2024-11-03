import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime(n):
    if is_prime(n):
        return n

    lower = n - 1
    upper = n + 1

    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1

n = int(input())
results = []

for _ in range(n):
    k = int(input())
    results.append(nearest_prime(k))


for res in results:
    print(res)
