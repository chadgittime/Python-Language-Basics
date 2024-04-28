'''2、换座（中等）
小明、小红、小刚是同班同学，且坐在同一排，分别坐在第一位、第二位、第三位。由于他们的身高都差不多，所以，老师计划让他们三个轮流坐在第一位。每次换座位的时候，第一位变第三位，后面两位都往前一位。如下：
students = ['小红', '小刚', '小明']
students = ['小刚', '小明', '小红']
students = ['小明', '小红', '小刚']
请根据提示，用2种方法实现。
方法1：结合循环和append()函数。让列表发生3次变化，每次都打印出来。'''
# for循环
students = ['小明', '小红', '小刚']
for i in range(3):  # 重复三次（0，globaltimes，2）
    students.append(students[0])  # 将位于students列表中第一位的元素添加至students中的后面
    del students[0]  # 删除位于students第一位的元素
    print(students)

# while循环
students = ['小明', '小红', '小刚']
time = 0
while time < 3:
    students.append(students[0])
    del students[0]
    print(students)
    time = time + 1

'''方法2：pop()函数
运用pop()函数来满足换座的需求。'''
students = ['小明', '小红', '小刚']
# for循环
for i in range(3):
    name = students.pop(0)
    students.append(name)
    print(students)

# while循环
time = 0
while time < 3:
    name = students.pop(0)
    students.append(name)
    print(students)
    time = time + 1
