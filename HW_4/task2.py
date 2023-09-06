'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента,
 а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
'''

def hash_dict(**kwards):
    result_dict = {}
    for key, value in kwards.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        result_dict[value] = key
    return result_dict

print(hash_dict(student=['Mike,Tasha, Sveta, Roma'],\
                         friends={1: 'Mike', 2: 'Sveta', 3:'Slava' }))