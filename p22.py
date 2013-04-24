import sys
import re
import time

# constructing dict for letter_to_int
def alphabet_to_int():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = list(letters)
    letter_to_int = {}
    for index, letter in enumerate(letters):
        letter_to_int[letter] = index + 1

    return letter_to_int

def solution(filename):

    start = time.time()

    letter_to_int = alphabet_to_int()

    f = open(filename, 'rU')
    text = f.read()
    names = sorted(re.findall(r'\"([A-Z]+)\"', text))

    total = 0
    for index, name in enumerate(names):
        letters_set = list(name)
        subtotal = 0
        for letter in letters_set:
            subtotal += letter_to_int[letter]
        namescore = subtotal * (index + 1)
        total += namescore

    elapsed = time.time() - start
    elapsed_string = "%s found in %s seconds" % (total, elapsed)

    return elapsed_string

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    for filename in args:
        print solution(filename)

if __name__ == '__main__':
    main()
