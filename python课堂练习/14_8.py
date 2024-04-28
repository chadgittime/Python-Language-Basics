class C0:
    name = 'C0'

    def name1(self):
        print("name='C0'")


class C1:
    num = 1

    def num1(self):
        print('num=globaltimes')


class C2(C0):
    num = 2

    def num1(self):
        print('num=2')


class C3:
    name = 'C3'

    def name1(self):
        print("name='C3'")


class C4(C1, C2, C3):
    pass


C4_1 = C4()
C4_1.name1()
C4_1.num1()
