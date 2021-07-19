
from math import sqrt, log, floor
#brute force method of summation of primes (project euler)

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

'''primes = []
res = 0
for i in range(2, 10):
    if isPrime(i):
        primes.append(i)
for i in primes:
    res += i
print(res)'''


# 2nd method (hackerrank solution)
# This method below is effective in cracking hackerrank test cases.

# This function prepares a sieve(list) only once till the given testcases i.e. 10000 in hackerrank.

def sieve_of_primes(n):
    last_index = (n - 1) // 2 + 1  
    sieve = [1] * last_index  
    sieve[0] = 0
    rtn = floor(sqrt(n)) // 2 + 1
    for i in range(1, rtn):
        if sieve[i]:
            for j in range(2 * i * (i + 1), last_index, 2 * i + 1):
                sieve[j] = 0

    return sieve  

'''
This function can be used but it needs to be called everytime. 
if we already created a sieve till 10 we can use that sieve and add on further
which will increase the performance.
def sum_of_primes(n, sieve):
    ps = 2
    for i in range((n - 1) // 2 + 1):
        p = 2 * i + 1
        if sieve[i]:
            ps += p
    return ps
'''

def prefix_sums_of_primes(l, sieve):
    ls = len(sieve)
    sums = [0] * (l + 1)
    sums[2] = 2
    ps = 2
    for i in range(ls):
        p = 2 * i + 1 # calculation of the prime numbers happens here.
        if sieve[i]:
            ps += p
        sums[p] = ps
        sums[p + 1] = ps
    return sums


sieve = sieve_of_primes(1000000)
sums = prefix_sums_of_primes(1000000, sieve)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sums[n])

