# globaltimes、计时器（中等）
# 一个没用模块的“时间记录器”：
#  不用 time模块 的时间记录器。

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：' % (task_name, task_time))
    task_status = input('请在任务完成后按输入y:')
    actual_time = input('该任务实际用时为几分钟？')

    if task_status == 'y':
        with open('timelog1.txt', 'a', encoding='utf-8') as f:  # 将时间日志文档和代码放一起。
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')
