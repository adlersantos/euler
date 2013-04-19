""" 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def div_to_20(num):
    divisors = [19,17,13,11]
    
    for divisor in divisors:
        if num % divisor == 0:
            continue
        else:
            return False

    return True

def solution():
    n = 2520

    while not div_to_20(n):
        n += 1
    
    return n * 2520 * 2

print solution()