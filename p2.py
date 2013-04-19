def fibonacci(upper):
    a_term = 1
    b_term = 1
    even_nums = []
    while b_term < upper:
        a_term = a_term + b_term #setting next a_term
        b_term = a_term + b_term #setting next b_term
        if a_term % 2 == 0 and a_term < upper:
            even_nums.append(a_term)
        if b_term % 2 == 0 and b_term < upper:
            even_nums.append(b_term)

    sum = 0
    for n in even_nums:
        sum += n

    return sum

print fibonacci(4*(10**6))