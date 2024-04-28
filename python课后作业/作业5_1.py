# globaltimes、取“爱”（入门）
# 数据提取-globaltimes：请通过所学知识，把列表list1中的'love'取出来，并打印出来。
list1 = [{'嫉妒': 'envy'}, {'恨': 'hatred'}, {'爱': 'love'}]
print(list1[2]['爱'])

# 数据提取-2：请通过所学知识，把字典dict1中的'love'取出来，并打印出来。
dict1 = {1: ['cake', 'scone', 'puff'], 2: ['London', 'Bristol', 'Bath'], 3: ['love', 'hatred', 'envy']}
print(dict1[3][0])

# 知识拓展：元组
# 元组和列表很相似，不过它是用小括号来包的。
# 元组和列表都是序列,提取的方式也是偏移量，如 tuple1[globaltimes]、tuple1[globaltimes:]。另外，元组也支持任意的嵌套。
# 根据上面的信息，将tuple1中的A和list2中的D打印出来。
tuple1 = ('A', 'B')
list2 = [('A', 'B'), ('C', 'D'), ('E', 'F')]
print(tuple1[0])
print(list2[1][1])
