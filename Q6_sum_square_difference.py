def square_sum_difference(limit):
    sum_num = limit * (limit + 1) // 2
    sum_squares = ((2*limit + 1) * (limit + 1) * limit) // 6

    return (sum_num ** 2) - sum_squares

#print((square_sum(100)))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(square_sum_difference(n))