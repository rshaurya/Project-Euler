from math import sqrt
def isPrime(num):
    x = int(sqrt(num))
    for j in range(2, x + 1):
        if num % j == 0:
            return False
    return True

#assert(isPrime(17))

def lcm_of_range(n):
    for i in range(2, n+1):
        if (isPrime(i)):
            print(i)

lcm_of_range(20)

