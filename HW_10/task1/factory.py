from animals import Animal, Dog, Cat, Birds

class Farm:
    parameters = {}

    @classmethod
    def build(cls, type_animal, name, age, spec):
        cls.parameters = dict(name=name, age=age, spec=spec)
        return cls._choice(type_animal)

    @classmethod
    def _choice(cls, type_animal):
        match type_animal:
            case 'Dog':
                return cls._create_dog(**cls.parameters)
            case 'Cat':
                return cls._create_cat(**cls.parameters)
            case 'Birds':
                return cls._create_birds(**cls.parameters)
            case _:
                return Animal('Fish', 15)

    @classmethod
    def _create_dog(cls, name, age, spec):
        return Dog(name=name, age=age, spec=spec)

    @classmethod
    def _create_cat(cls, name, age, spec):
        return Cat(name=name, age=age, spec=spec)

    @classmethod
    def _create_birds(cls, name, age, spec):
        return Birds(name=name, age=age, spec=spec)


def main():
    dog = Farm.build('Dog', 'Flounder', 5, 'Игривый')
    birds = Farm.build('Bird', 'Chichi', 8, 'Певчая птичка')
    cat = Farm.build('Cat', 'Tom', 3, 'Разноцветный')
    unknown = Farm.build('Non-type', 'noname', 'unknow', 'uncheck')

    animals = (dog, birds, cat, unknown)
    for animal in animals:
        print(animal.get_info())


if __name__ == '__main__':
    main()
