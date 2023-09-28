__all__ = ["Animal", "Dog", "Cat", "Birds"]


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_info(self):
        return (f'{"Type:"}{type(self).__name__}'
                f'\n{"Name:"}{self.name}'
                f'\n{"Age:"}{self.age} years')

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def get_info(self):
        return (super().get_info())


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def get_info(self):
        return (super().get_info())


class Birds(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def get_info(self):
        return (super().get_info())


# pet_1 = Dog('Tom', 5, 'лает')
# pet_2 = Cat('Fill', 2, 'мурчит')
# pet_3 = Birds('Jack', 1, 'чирикает')
#
# for pet in [pet_1, pet_2, pet_3]:
#     print(f'{pet.name} {pet.get_spec()}')
#     print(f'{pet.get_info()}')
#
# if __name__ == '__main__':
#     print('Not for separate use')
