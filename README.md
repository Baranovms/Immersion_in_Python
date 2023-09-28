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
### hw_6

#### task1
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
#### task2
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
#### task3
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#### task4
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

---------------
---------------

### hw_7

#### zadanie4
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
-расширение
-минимальная длина случайно сгенерированного имени, по умолчанию 6
-максимальная длина случайно сгенерированного имени, по умолчанию 30
-минимальное число случайных байт, записанных в файл, по умолчанию 256
-максимальное число случайных байт, записанных в файл, по умолчанию 4096
-количество файлов, по умолчанию 42
-Имя файла и его размер должны быть в рамках переданного диапазона.

#### zadanie5
Доработаем предыдущую задачу.
-Создайте новую функцию которая генерирует файлы с разными расширениями.
-Расширения и количество файлов функция принимает в качестве параметров.
-Количество переданных расширений может быть любым.
-Количество файлов для каждого расширения различно.
-Внутри используйте вызов функции из прошлой задачи.

#### zadanie6
Дорабатываем функции из предыдущих задач.
-Генерируйте файлы в указанную директорию — отдельный параметр функции.
-Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
-Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

#### zadanie7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

#### task1
Напишите функцию группового переименования файлов. Она должна:
-принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
-принимать параметр количество цифр в порядковом номере.
-принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
-принимать параметр расширение конечного файла.
-принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
-Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

---------------
---------------

### hw_8

Решить задания, которые не успели решить на семинаре.

#### task1

Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов

---------------
---------------

### hw_9

#### task1
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


---------------
---------------

### hw_10

#### task1
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

#### task2
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.