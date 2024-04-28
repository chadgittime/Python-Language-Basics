file1 = open('scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

final_scores = []

for i in file_lines:
    data = i.split()
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换    
    result = data[0] + str(sum) + '\n'  # 结果就是学生姓名和总分
    print(result)
    final_scores.append(result)

print(final_scores)

sum1 = open('winner.txt', 'w', encoding='utf-8')
sum1.writelines(final_scores)
sum1.close()
