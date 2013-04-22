"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
from collections import defaultdict

def dn_sets(n): #dict of n, d(n)
    dn_sets = {}

    for i in range(2, n + 1): # excluding 1, will add it
        dn = 0
        divisors = []
        for divisor in range(1, i/2 + 1):
            if i % divisor == 0:
                dn += divisor
        dn_sets[i] = dn

    return dn_sets

def solution():
    start = time.time()

    amicable_numbers = []
    dn_dict = dn_sets(10000)

    for numkey in dn_dict:
        b = dn_dict[numkey]
        if b in dn_dict:
            a = dn_dict[b]
            if (b != a) and (numkey == a):
                amicable_numbers.append(b)
                amicable_numbers.append(a)

    answer = sum(list(set(amicable_numbers)))

    elapsed = time.time() - start
    elapsed_string = "found in %s seconds" % (elapsed)

    return answer, elapsed_string

print solution()