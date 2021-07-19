from math import ceil, sqrt

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)


def pythagorean_triplet(s):
    s2 = s // 2
    mlimit = ceil(sqrt(s2)) - 1
    for m in range(2, mlimit):
        if s2 % m == 0:
            sm = s2 // 2
            while sm % 2 == 0:
                sm = sm // 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 // k*m
                    n = k - m
                    a = d * (m**2 - n**2)
                    b = s * d * m * n
                    c = d * (m**2 + n **2)
                    return a,b,c
                k += 2
        else:
            return -1

def product_of_triplets(s):
    n = (s - 3) // 3
    for a in range(3, n):
        for b in range((a + 1), (s - 1 - a) // 2):
            c = s - a - b
            if c*c == a*a + b*b:
                return a * b * c


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(product_of_triplets(n))

