#completed
yr = int(input('Insert a year: '))


def is_leap(year):
    if(year%4 == 0 or year%400 ==0):
        print(True)
    else:
        print(False)


is_leap(yr)