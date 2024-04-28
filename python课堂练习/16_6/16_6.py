# 统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。注意，这个练习的全程只能用Python。
f = open('scores.txt', 'r')
all_scores = f.readlines()
final_scores = []
for scores in all_scores:
    total_score = 0
    scores = scores.split(' ')
    for score in scores[1:]:
        total_score = total_score + int(score)
    # 此处也可以用isdigit
    #       if score.isdigit():
    #           total_score = total_score + int(score)
    final_score = scores[0] + str(total_score) + '\n'
    final_scores.append(final_score)
f.close()

with open('final_scores.txt', 'a') as file:
    file.writelines(final_scores)
