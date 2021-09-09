

def dayOfProgrammer(year):
    mon_day = [10]
    if year > 1918:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            num = '{:0=2d}.{:0=2d}.{}'.format(mon_day[0] + 2, mon_day[0] - 1, year)

        else:
            num = '{:0=2d}.{:0=2d}.{}'.format(mon_day[0] + 3, mon_day[0] - 1, year)

    if year < 1918:
        if year % 4 == 0:
            num = '{:0=2d}.{:0=2d}.{}'.format(mon_day[0] + 2, mon_day[0] - 1, year)

        else:
            num = '{:0=2d}.{:0=2d}.{}'.format(mon_day[0] + 3, mon_day[0] - 1, year)

    if year == 1918:
        num = '{:0=2d}.{:0=2d}.{}'.format(mon_day[0] + 16, mon_day[0] - 1, year)

    return num


print(dayOfProgrammer(2016))


# for i in range(1700, 2701):
#     if dayOfProgrammer(i) :
#         print(dayOfProgrammer(i))

