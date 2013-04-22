import time

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

def days_in_month(month_num, year):
    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if month_num == 2 and is_leap_year(year):
        return 29
    else:
        return month_days[month_num]

def solution():

    day_counter = 0
    first_sundays = 0
    first_sundays_1900 = 0
    
    start = time.time()

    for i in range(1900, 2001): # for years
        month_days = []
        for j in range(1, 13): # populating month days
            day_counter += days_in_month(j, i)
            if (day_counter + 1) % 7 == 0:
                first_sundays += 1
                if i == 1900:
                    first_sundays_1900 += 1

    answer = first_sundays - first_sundays_1900

    elapsed = time.time() - start
    elapsed_string = "found in %s seconds" % (elapsed)


    return answer, elapsed_string

print solution()