"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(num):
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution():

    primes = [2, 3, 5, 7, 11, 13]
    n = 13

    while len(primes) != 10001:
        n += 2
        for prime in primes:
            if n % prime == 0:
                break
            if prime == primes[-1]:
                primes.append(n)

    return primes[-1]

print solution()