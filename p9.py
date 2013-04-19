"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_pyth_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def is_sum(total, *args):
    if sum(args) == total:
        return True
    else:
        return False

def solution():
    triplet = []

    for i in range(1,999):
        for j in range (1,999):
            if i + j < 1000:
                k = 1000 - i - j
                triplet = sorted([i, j, k])

                a, b, c = triplet
                if is_pyth_triplet(a, b, c):
                    return a*b*c

print solution()