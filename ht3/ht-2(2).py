year_start, year_end = int(input()), int(input())

for i in range(year_start, year_end + 1):
    if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
        print(i)