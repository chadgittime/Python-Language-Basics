'''
提示1：photo1的图片若与代码文件是位于同一个文件夹下，可直接写文件名即可（注意有后缀）。
提示2：可用课堂末尾提到的with open...as这种语句来进行文件读写，注意缩进。
提示3：因为图片是以二进制的形式保存的，所以读写时需要用 rb 和 wb模式。
'''

with open('/Users/tomatotaco1/PycharmProjects/pythonProject/python课后作业/作业16_1/photo1.png','rb') as file1:
    content=file1.read()

with open('/Users/tomatotaco1/PycharmProjects/pythonProject/python课后作业/作业16_1/photo2.png','wb') as file2:
    file2.write(content)

