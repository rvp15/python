class Person:
    # constructor/initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def display_info(self):
        print(f'Person name:{self.name}, Age:{self.age}')


# create obj
person1 = Person('vedha', 34)
person2 = Person('Sudi', 10)

person1.display_info()
person2.display_info()
