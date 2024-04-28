# 【文件：B.py】
from test import hi  # 从模块test中导入函数“hi”

hi()

# 以下语句将会导致报错，因为并没有导入test模块，只是导入test模块中的函数“hi”
test.hey()
