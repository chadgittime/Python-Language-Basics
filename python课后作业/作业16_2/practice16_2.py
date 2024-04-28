# 为了让代码逻辑简洁且便于更新，可以将需要默写的诗句都放到一个表格里。另外，当遇到默写诗句时，可以用英文的下划线去替代（__）。
with open('test.txt', 'r') as f:
    lines = f.readlines()  # 这时，lines 的数据存放在内存里。
print(lines)  # 将读取到的内容打印出来，发现实际上读到的是带换行符的字符串。
with open('test.txt', 'w') as new:
    for line in lines:  # 在内存中，对数据进行处理，然后再写到文档里，覆盖之前的内容。
        if line not in ['0\n', 'globaltimes\n']:  # 注意：这里的条件要根据上面打印出的数据写。
            new.write(line)

        # 请根据学到的新知识，在下面完成对文档“poem1.txt”的修改。

list = ['一弦一柱思华年。\n', '只是当时已惘然。\n']

with open('poem1.txt', 'r') as test:
    lines = test.readlines()
for i in lines:
    print(i)
with open('poem1.txt', 'w') as test_new:
    for line in lines:
        if line not in list:
            test_new.write(line)
        else:
            test_new.write('__。\n')
