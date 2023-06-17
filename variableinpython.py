# local variable: defined and accessed only inside a specific block
# global variable: defined globally & accessed anywhere in program
# instance variable: are specific to an instance(object), defined inside class, each objs will have different values
# class variable: defined inside class but outside anymethod.shared by all instance of a class, same value for all objects
#  static variables: same as class, but defined with @staticmethod, same value for all obj
# constants: value is unchanged, specify in uppercase


# instance variable: variables passed to each object instance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}")


# Create an instance of the Car class
my_car = Car("Toyota", "Camry")

# Access and modify instance variables
print(my_car.brand)  # Output: Toyota

# Create another instance of the Car class
your_car = Car("Honda", "Civic")

print(your_car.brand)  # Output: Honda


# Class variable:
# Class variables are defined directly within the class body and are typically used to store data that is common to all instance
# Accessed by Car.count === classname.variablename
class Car:
    # class variable
    car_count = 0

    def __init__(self, brand):
        self.brand = brand
        Car.car_count += 1

    def drive(self):
        print(f'starting{self.brand}')


car1 = Car('honda')
car2 = Car('Tesla')

print(car1.brand)
print(Car.car_count)

Car.car_count = 6