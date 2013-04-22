import time

def solution():

    product = 1
    for i in range(1, 101):
        product *= i

    product_str = str(product)
    product_len = len(product_str)

    total = 0
    for i in range(product_len):
        digit = product_str[i]
        digit_int = int(digit)
        total += digit_int

    return product_str, product_len, total

print solution()