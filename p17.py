def num_to_phrase(num):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    elevens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['none', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'

    numstring = str(num)

    if num < 10:
        return ones[num]
    elif 10 <= num < 20:
        return elevens[num % 10]
    elif 20 <= num < 100:
        if num % 10 == 0:
            return tens[num / 10]
        else:    
            return tens[num / 10] + num_to_phrase(num % 10)
    elif 100 <= num < 1000:
        if num % 100 == 0:
            return ones[num / 100] + 'hundred'
        else:
            return ones[num / 100] + 'hundredand' + num_to_phrase(num % 100)
    elif num == 1000:
        return 'onethousand'

def solution():
    total = 0

    for i in range(1, 1001):
        numstring = num_to_phrase(i)
        total += len(numstring)

    return total

print solution()