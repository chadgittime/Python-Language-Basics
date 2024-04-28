#阅读、运行代码，观察结果

class Computer:
    screen = True

    def start(self):
        print('电脑正在开机中……')

my_computer = Computer()
print(type(my_computer))
print(my_computer.screen)
my_computer.start()