## Immersion_in_Python

---------------
### hw_1

#### task1
- Вывести в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

#### task2
- Треугольник существует только тогда, когда сумма любых двух его сторон больше
третьей. Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить
длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае
отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
существует.
- Отдельно сообщить, является ли треугольник разносторонним, равнобедренным или равносторонним.

#### task3
- Написать код, который запрашивает число и сообщает, является ли оно простым или составным. Использовать правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
- Сделать ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
---------------
---------------
### hw_2

### zadanie_6
- Напишите программу банкомат. 

✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

#### task1
- Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.

#### task2
- Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.

---------------
---------------
### hw_3

### zadanie_8
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.

#### task1
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

#### task2
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

#### task3
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

---------------
---------------
### hw_4

#### task1
Напишите функцию для транспонирования матрицы


#### task2
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

#### task3
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

---------------
---------------
### hw_5

#### task1
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».

#### task2
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.

#### task3
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии

#### task4
Создайте функцию генератор чисел Фибоначчи (см. Википедию).

---------------
---------------