# 定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
# 最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'
def reward(month):
    if 0 < month < 6:
        return 500
    elif 6 <= month <= 12:
        return 120 * month
    elif month > 12:
        return 180 * month


def payroll(name, month):
    if 0 < month:
        print("{}来了{}个月，获得奖金{}元。".format(name, month, reward(month)))
    else:
        print("月份有误！")


payroll("大聪", 14)
