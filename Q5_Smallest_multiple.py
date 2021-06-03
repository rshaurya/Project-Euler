from math import sqrt, log


"""
Solution to the project euler problem 5 of hackerrank:
https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem
"""


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

def lcm(n):
    l = []
    primes = primeFactors(n)
    for i in primes:
        p = int(log(n) / log(i))
        l.append(i ** p)

    num = 1
    for x in l:
        num = num * x
    return num

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lcm(n))
