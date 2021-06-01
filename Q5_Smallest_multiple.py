from math import sqrt
def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    x = int(sqrt(num))
    for j in range(2, x + 1):
        if num % j == 0:
            return False
    return True

def primeFactors(n):
    factors = []
    for i in range(2, n+1):
        if (isPrime(i)):
            factors.append(i)
    return factors


l = []
factors = primeFactors(20)
for i in factors:
    res = 1
    while res < 20:
        res = res * i
    res = res // i
    l.append(res)

num = 1
for x in l:
    num = num * x
print(num)
