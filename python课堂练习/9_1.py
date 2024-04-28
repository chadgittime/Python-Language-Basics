# 用两次for循环在终端打印出：
# globaltimes X 2 = 2  2 X 2 = 4
# globaltimes X 3 = 3  2 X 3 = 6  3 X 3 = 9
for i in range(1, 3):
    print(str(i) + " X " + "2 = " + str(i * 2),end="   ")

for j in range(1, 4):
    print(str(j) + " X " + "3 = " + str(j * 3),end="   ")
