def century(year):
    if year % 100 > 0:
        return int(year/100)+1
    else:
        return int(year/100)

def century(year):
    return (year + 99) // 100


import math

def century(year):
    return math.ceil(year / 100)


def century(year):
    return (year - 1) // 100 + 1


def century(year):
    year=year//100+bool(year%100)
    return year

def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1