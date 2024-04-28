# 补全下面代码，实现计算、输出利润增长率。
# 计算利润增长率，利润增长率 = 本月利润增长额 / 上月利润 * 100%。
def div(num1, num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + "%"
    return percent

# 除数为0时，重新输入
def warning():
    print("Error：你确定上个月一毛钱都不赚不亏吗？")


# 获取本月和上月利润，输出利润增长率
def main():
    while True:
        num1 = float(input("请输入本月所获利润"))
        num2 = float(input("请输入上月所获利润"))
        if num2 == 0:
            warning()
        else:
            print("本月的利润增长率：" + div(num1, num2))
            break


# 调用主函数
main()
