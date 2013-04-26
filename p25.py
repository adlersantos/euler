import time

def fibonacci():

    start = time.time()

    nums = [1, 1]
    total = 0
    n = 1
    while len(str(total)) < 1000:
        n += 1
        total = nums[n-1] + nums[n-2]
        nums.append(total)

    elapsed = time.time() - start
    elapsed_string = "%s found in %s seconds" % (n + 1, elapsed)

    return elapsed_string

print fibonacci()


