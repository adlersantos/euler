"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 99. 

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome():
    palindrome = 0
    factors = []

    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            product = i * j
            string_num = str(product)

            if string_num == string_num[::-1]:
                if product > palindrome:
                    palindrome = product
                    factors = [i,j]

    return palindrome, factors

print largest_palindrome()