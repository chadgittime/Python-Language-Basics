# 阅读直接运行代码。
class Teacher:
    face = 'serious'
    job = 'teacher'


class Father:
    face = 'sweet'
    parenthood = 'dad'


time1 = Teacher()  # 在time1这个时刻，那个男人角色是老师。
time2 = Father()  # 在time2这个时刻，那个男人角色是父亲。
print(time1.face)  # 时刻不同，角色不同，脸也不同。
print(time2.face)


class TeacherMore(Teacher):
    face = 'gentle'


class FatherMore(Father):
    pass


time3 = TeacherMore()
time4 = FatherMore()
print(time3.face)
print(time4.face)
