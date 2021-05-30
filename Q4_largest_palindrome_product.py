def is_Palindrome(n):
    original = n
    res = 0
    while n > 0:
        n, r = divmod(n, 10)
        res = res * 10 + r
    return res == original

    
def largest_palindrome(new):
    maxp = 0
    for i in range(990, 100, -11):
        for j in range(999, 100, -1):
            if i*j < maxp or i*j >= new:
                continue
            if is_Palindrome(i * j):
                maxp = max(maxp, i*j)

    return maxp

print(largest_palindrome(800000))
print(largest_palindrome(101110))

print(largest_palindrome(101101))
