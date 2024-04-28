# 请在一个叫1.txt文件里写入字符串'难念的经'，然后请读取这个16_5的附属品.txt文件的内容，并打印出来。
f = open("16_5的附属品.py", 'a')
f.write("难念的经")
f.close()

f = open("16_5的附属品.py", 'r')
content = f.read()
print(content)
f.close()
