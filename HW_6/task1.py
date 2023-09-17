from sys import argv

_END_DAY_31= 31
_END_DAY_30 = 30
_END_DAY_FEB = 28
_START_DAY = 1
_END_YEAR = 9999
_START_YEAR = 1

def check_date(date):
    day, month, year = map(int, date.split('.'))
    if _START_YEAR <= year <= _END_YEAR:
        if month in [1, 3, 5, 7, 8, 10, 12] and _START_DAY <= day <= _END_DAY_31:
            return True
        elif month in [4, 6, 9, 11] and _START_DAY <= day <= _END_DAY_30:
            return True
        elif _END_DAY_FEB <= day <= _END_DAY_FEB + is_leap_year(year):
            return True
        else:
            return False
    return False


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def check_in_terminal():
    date = argv[1]
    print('Верная дата' if check_date(date) else 'Такой даты не может быть')

# date = input('ВВедите дату в формате дд.мм.гггг: ')
# print('Верная дата' if check_date(date) else 'Такой даты не может быть')