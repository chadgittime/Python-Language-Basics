# globaltimes.分别使用gbk和utf-8编码自己的名字，并将其打印出来。

# 2.复制上一步得到的结果，进行解码，打印出你的名字（两次）。

print('郭悦洋'.encode('gbk'))
print('郭悦洋'.encode('utf-8'))

for i in range(1, 3):
    print(b'\xb9\xf9\xd4\xc3\xd1\xf3'.decode('gbk'))
    print(b'\xe9\x83\xad\xe6\x82\xa6\xe6\xb4\x8b'.decode('utf-8'))
