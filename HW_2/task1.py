
'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

numb = int(input("введите целое число: "))
base = 16
num = abs(numb)
new_numb = ''

str_ = "0123456789abcdef"
while num:
    num_char = str_[num % base]
    new_numb = num_char + new_numb
    num //= base
if numb < 0:
    new_numb = "-" + new_numb
if numb == 0:
    new_numb = "0"

print(f'          Число {numb} в {base}-ой системе счисления = {new_numb}')
print(f'Проверка: число {numb} в 16-ой системе счисления = {hex(numb)[2:]}')