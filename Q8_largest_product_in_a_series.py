
def largest_prod_in_a_series(l, k): # n is a string
    res = 0
    starting_slice = 0
    end_slice = k
    s = ''
    while end_slice <= len(l):
        s = l[starting_slice:end_slice]
        starting_slice += 1
        end_slice += 1
        if '0' in s:
            continue
        num = int(s)
        prod = 1
        while num > 0:
            r = num % 10 #taking out last digit
            num = num // 10 #taking out all digits except the last one
            prod = prod * r
        if res < prod:
            res = prod
    return res


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ') # k consecutive digits, in a n digit number.
    n,k = [int(n),int(k)] # converted into integers
    number = input().strip() # the number to perform operations with 
    print(largest_prod_in_a_series(number, k))

    