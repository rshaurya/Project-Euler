from math import log


def nth_prime_number(n):
    num_prime = int(2 * n * log(n)) #formula
    primes = [1] * num_prime #list of length of num_prime with all elements as 1.
    count = 0 #count is the ith number 
    for i in range(2, num_prime): #i is the index
        if primes[i]:
            count += 1
        if count == n:
            print("i is returning")
            return i
        for j in range(2*i, num_prime, i): #putting all multiples of the prime as 0
            primes[j] = 0
    

print(nth_prime_number(10001))