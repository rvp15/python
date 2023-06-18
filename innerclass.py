class OuterClass:
    def __init__(self):
        self.outer_attr = 'Outer attribute'

    def outer_method(self):
        print('This is the outer method')

    class InnerClass:
        def __init__(self):
            self.inner_attr = 'Inner attribute'

        def inner_method(self):
            print('This is the inner method')


# Creating an instance of the outer class
outer_obj = OuterClass()

# Accessing outer class attributes and methods
print(outer_obj.outer_attr)
outer_obj.outer_method()

# Creating an instance of the inner class
inner_obj = outer_obj.InnerClass()

# Accessing inner class attributes and methods
print(inner_obj.inner_attr)
inner_obj.inner_method()

# u have to create obj for outer class and with help of outer instance(obj) you can access inner class

# innerObj = outerObj.Innerclass()    -> with this inner obj u can access inner attributes and methods
