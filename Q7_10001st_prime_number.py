
from math import log, floor, sqrt

def nth_prime_number(n):
    num_prime = int(2 * n * log(n)) + 1 #formula
    primes = [1] * num_prime #list of length of num_prime with all elements as 1.
    count = 0 #count is the ith number 
    if n == 1:
        return 2
    for i in range(2, num_prime + 1): #i is the index
        if primes[i]:
            count += 1
            for j in range(2*i, num_prime, i): #putting all multiples of the prime as 0
                primes[j] = 0
        if count == n:
            return i

print(nth_prime_number(2))

def isPrime_optimised(n):
    if n == 1: #1 is not a prime number
        return False
    elif n < 2: 
        return False
    elif n < 4: # the only prime number less than 4 are 2 and 3
        return True
    elif n % 2 == 0: # 2 is the only even number
        return False
    elif n % 3 == 0:
        return False
    else:
        res = floor(sqrt(n)) # round-off to the greatest integer
        f = 5
        while f <= res:
            if n % f == 0:
                return False 
            if n % (f + 2) == 0:
                return False
            f += 6
    return True


def nth_prime_method_two(limit):
    count = 1
    r = 1
    for i in range(1, limit + 1):
        if count == limit:
            return r
        r += 2
        if isPrime_optimised(r):
            count += 1
    return res 


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(nth_prime_method_two(n))