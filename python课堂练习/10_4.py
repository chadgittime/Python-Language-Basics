# 写一个跟len()函数功能相同、能计算字符串长度的函数，传递参数'三根皮带，四斤大豆'来调用函数，并将结果打印出来。
def my_len(words):
    timer = 0
    for i in words:
        timer = timer + 1
    return timer


print(my_len('三根皮带，四斤大豆'))
