def square_sum(num):
    sum_of_squares = 0
    square_of_sum = 0
    sum = 0
    difference = 0
    for i in range(1, num + 1):
        sum_of_squares += i ** 2
    for k in range(1, num + 1):
        sum += k
    square_of_sum = sum ** 2

    return square_of_sum - sum_of_squares

print((square_sum(100)))
