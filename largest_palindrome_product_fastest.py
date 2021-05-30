def is_palindrome(n):
    original = n
    res = 0
    while n > 0:
        n, r = divmod(n, 10)
        res = res * 10 + r
    return res == original

print(is_palindrome(1212))
