'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

max_limit = 100_000
min_limit = 0

while True:
    input_numb = int(input('Введите число: '))
    if input_numb < min_limit or input_numb > max_limit:
        print(f'Введите значение в диапазоне от {min_limit} до {max_limit}')
    else:
        break

if input_numb == 0 or input_numb == 1:
    print(f'число {input_numb} - является ни простым, ни составным')
else:
    count = 0
    for i in range(1, input_numb):
        if input_numb % i == 0:
            count += 1
    if count >= 3:
        print(f'число {input_numb} - является составным')
    else:
        print(f'число {input_numb} - является простым')
