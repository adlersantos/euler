import time

def is_repeating(d):
    length = 0
    remainders = []
    for i in range(1, d): # fact that 1/d may contain a recurring term up to d-1 digits
        remainder = 10**i % d
        remainders.append(remainder)
        if 1 == remainder:
            length = i
            return True, length
    
    if len(list(set(remainders))) == 1:
        return True, 1
    else:
        return False, 0

def solution():

    start = time.time()

    max_length = 0
    answer = 0
    for d in range(2, 1000):
        if is_repeating(d)[0] and max_length < is_repeating(d)[1]:
            max_length = is_repeating(d)[1]
            answer = d

    elapsed = time.time() - start
    elapsed_string = "%s with recurring term length %s, found in %s seconds" % (answer, max_length, elapsed)

    return elapsed_string

print solution()
