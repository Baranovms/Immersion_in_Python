class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def validate_name(self, name):
        if not name.isalpha():
            raise InvalidNameError(f"Invalid name: {name}")

    def validate_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError(f"Invalid age: {age}")

    def validate_data(self):
        self.validate_name(self.last_name)
        self.validate_name(self.first_name)
        self.validate_name(self.patronymic)
        self.validate_age(self.age)

    def birthday(self):
        self.age += 1
        
    def get_age(self):
        return f'{self.age}'


class Employee(Person):
    def __init__(self, last_name, first_name, patronymic, age, id):
        super().__init__(last_name, first_name, patronymic, age)
        self.id = id

    def validate_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise InvalidIdError(f"Invalid ID: {id}")

    def validate_data(self):
        super().validate_data()
        self.validate_id(self.id)

    def get_level(self):
        return sum(int(digit) for digit in str(self.id)) % 7
    

    
person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())