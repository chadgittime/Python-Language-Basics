# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。
# 字符串内的字符也是可以通过偏移量进行提取的（具体的提取和切片的方法和列表一致）。

file1 = open('winner.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()
dict_scores = {}
list_scores = []
final_scores = []

# \n也算一个字符
for i in file_lines:
    name = i[:-4]
    score = i[-4:-1]
    dict_scores[score] = name
    list_scores.append(score)
list_scores.sort(reverse=True)
for i in list_scores:
    final_scores.append(dict_scores[i] + i + '\n')

with open('winner_new.txt', 'a', encoding='utf-8') as f:
    f.writelines(final_scores)
