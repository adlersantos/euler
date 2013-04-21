import operator

def step(num):
    if num % 2 == 0:
        return num/2
    else:
        return 3*num + 1

def solution():

    answer = 0
    answer_key = 0
    starting_num_dict = {}

    for i in range(2, 1000000):
        result = i
        num_steps = 1
        while result != 1:
            result = step(result)
            num_steps += 1
            if result in starting_num_dict:
                num_steps += starting_num_dict[result] - 1
                starting_num_dict[i] = num_steps
                break
            starting_num_dict[i] = num_steps

    for key in starting_num_dict:
        if starting_num_dict[key] > answer:
            answer = starting_num_dict[key]
            answer_key = key

    return answer_key

print solution()