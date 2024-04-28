# 如果==左右两边相等，值为True，不相等则为False。
print(1 == 1)
# 1等于1，所以值为True

print(1 == 2)
# 1不等于2，所以为False

students1 = ['小明','小红','小刚']
students2 = ['小刚','小明','小红']
print(students1 == students2)
#False
scores1 = {'小明':95,'小红':90,'小刚':100}
scores2 = {'小刚':100,'小明':95,'小红':90}
print(scores1 == scores2)
#True
