'''
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
'''

from math import *
from fractions import *

str1 = input('Введите первую дробь через /: ')
str2 = input('Введите вторую дробь через /: ')


def reduction_fract(numerator: int, denominator: int):
    if numerator > denominator:
        temp = numerator
    else:
        temp = denominator
    while temp != 1:
        if numerator % temp == 0 and denominator % temp == 0:
            return str(numerator // temp) + "/" + str(denominator // temp)
        else:
            temp -= 1
    return str(numerator) + "/" + str(denominator)


def sum_fract(str1, str2):
    numerator = str1.split('/')
    denominator = str2.split('/')
    noz_fraction = lcm(int(numerator[1]), int(denominator[1]))
    numerator_fraction_1 = int(noz_fraction / int(numerator[1]) * int(numerator[0]))
    numerator_fraction_2 = int(noz_fraction / int(denominator[1]) * int(denominator[0]))
    return reduction_fract(numerator_fraction_1 + numerator_fraction_2, noz_fraction)


def product_fract(str1, str2):
    numerator = str1.split('/')
    denominator = str2.split('/')
    return reduction_fract(int(numerator[0]) * int(numerator[0]), int(denominator[1]) * int(denominator[1]))


print("Расчет по программе:")
print(f'{str1} * {str2} = {product_fract(str1, str2)}')
print(f'{str1} + {str2} = {sum_fract(str1, str2)}')

print("\nПроверка по Fraction:")
print(
    f"{str1} * {str2} = {Fraction(int(str1.split('/')[0]), int(str1.split('/')[1])) * Fraction(int(str2.split('/')[0]), int(str2.split('/')[1]))}")
print(
    f"{str1} * {str2} = {Fraction(int(str1.split('/')[0]), int(str1.split('/')[1])) + Fraction(int(str2.split('/')[0]), int(str2.split('/')[1]))}")
