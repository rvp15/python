class A:
    def feature1(self):
        print('Freature 1 is working')

    def feature2(self):
        print('Freature 2 is working')


class B:
    def feature3(self):
        print('Freature 3 is working')

    def feature4(self):
        print('Freature 4 is working')
class C(A,B):
    # multiple inheritance
    def feature5(self):
        print('Freature 5 is working')

obj1 = A()
obj1.feature1()
obj1.feature2()

obj2 = B()
obj2.feature3()

obj3 = C()
obj3.feature1()
