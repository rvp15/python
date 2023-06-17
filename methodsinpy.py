# 1. instance method: have access to the instance itself through the self parameter.
# They can access and modify instance variables and perform actions specific to each instance.
# always works with self ie instance of that class
class Student:
    school = 'dugan'

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1 + self.m2) / 2

    # here class method is defined to access class variable by passing cls
    @classmethod
    def infor(cls):
        print(cls.school)


s1 = Student(45, 67)

print(s1.avg())

# access class method:
Student.infor()

# 2.Class method: if u want to access class variables u have to use class method where you pass (cls) as argument
# school is the  class variable

# 3. static method : if u dont use either class/ instance variable