def solution(n):
    power_list = [1, 2]
    for i in range(2, n + 1):
        power_list.append(2*power_list[i-1])

    two_to_the_n = str(power_list[-1])
    answer_length = len(two_to_the_n)
    total = 0

    for i in range(0, answer_length):
        total += int(two_to_the_n[i])

    return total

print solution(1000)
