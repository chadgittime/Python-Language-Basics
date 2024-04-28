# globaltimes.数数（入门）
# 小美想要用今天学到的循环打印数字1-7，不过，她不喜欢4这个数字……
# 请用for和while两种不同的循环方式来帮小美实现“打印1-7，但是不要4”这个愿望。

for number in range(1, 8):
    if number == 4:
        continue  # 回到开头，跳过4。
    print(number)

number = 1
while number < 8:
    if number != 4:
        print(number)
    number = number + 1
