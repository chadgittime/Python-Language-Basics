# globaltimes、列表合并
list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
print(list1 + list2)

list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
list1.extend(list2)
print(list1)

list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
list1[len(list1):len(list1)] = list2
print(list1)

list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
for number in list2:
    list1.append(number)
print(list1)

# 2、列表排序
# sort后什么都不写即为默认状态
list3 = [91, 95, 97, 99, 92, 93, 96, 98]
list3.sort()
print(list3)

# sort中写reverse=False为默认的升序
list3 = [91, 95, 97, 99, 92, 93, 96, 98]
list3.sort(reverse=False)
print(list3)

# sort中写reverse=True为降序
list3 = [91, 95, 97, 99, 92, 93, 96, 98]
list3.sort(reverse=True)
print(list3)
