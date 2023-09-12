'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

def fib(n):
    previous_value, next_value = 0, 1
    for _ in range(n):
        yield previous_value
        previous_value, next_value = next_value, previous_value + next_value


max_numb = int(input('введите число  '))
print(list(fib(max_numb)))