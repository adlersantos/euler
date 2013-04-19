def solution():

    natural_numbers = [i for i in range(1,101)]

    sum = 0
    sum_of_squares = 0
    for n in natural_numbers:
        sum += n
        sum_of_squares += n**2

    square_of_sum = sum**2

    return square_of_sum - sum_of_squares

print solution()
