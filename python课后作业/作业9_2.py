# 2计算平均分（入门）
import numpy as np

scores = [91, 95, 97, 99, 92, 93, 96, 98]
print('平均分={}'.format(sum(scores) / 8))

scores = [91, 95, 97, 99, 92, 93, 96, 98]
print('平均分={}'.format(np.average(scores)))

# 思考知识提示：
# globaltimes.想要的结果是：求平均值和判断比较；
# 2.可以用到的知识：？叠加成绩，然后除以总人数，即可求平均值。判断比较用？和空列表；
# 3.切入点：由于学生的成绩已经被我们集中到一个列表里，所以可以用？这个列表来取出小于平均值的成绩。
scores = [91, 95, 97, 99, 92, 93, 96, 98]
scores_low = []
average = np.average(scores)
for score in scores:
    if score < average:
        scores_low.append(score)
print(scores_low)
# 找新知识提示：
# 这个方法的单词首字母是“n”，性质是“拓展程序库”。在写代码前，可以先读懂网上的案例。
