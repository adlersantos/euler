"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
import itertools

numset = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def lexicographic_order(nums, position):

    start = time.time()

    permutations = list(itertools.permutations(nums, len(nums)))
    answer = ''

    nth_permute = permutations[position - 1]
    for num in nth_permute:
        answer += str(num)

    elapsed = time.time() - start
    elapsed_string = "%s found in %s seconds" % (int(answer), elapsed)

    return elapsed_string

print lexicographic_order(numset, 1000000)