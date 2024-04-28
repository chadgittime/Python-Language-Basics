#请用while True写一段程序，功能是请用户输入密码，如果输入了错误的密码，就一直循环请用户继续输入；如果输入了正确的密码，就结束循环。设定这个密码为'小龙女' 。通过后给出通过提示。
while True:
    password=input("请输入正确的密码：")
    if password=='小龙女':
        break
print('成功登陆')
