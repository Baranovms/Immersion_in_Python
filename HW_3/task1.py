'''
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''

list_1 = [1, 1, 2, 2, 3, 3, 4, 5, 6]
my_set = set()

for item in list_1:
    if list_1.count(item) > 1:
        my_set.add(item)
print("Исходный список", list_1)
print("Результирующий список", list(my_set))
