"""
模块的概念
    模块就是一个工具包，导入对应的模块就能使用模块中的工具
    每个py文件就是一个模块

导入模块：import 模块名
        注意：数字开头的模块名无法使用import关键字导入
        如果解释器发现import关键字，会将对应的模块解释后的字节码文件放到__pycache__文件夹中，提升程序的速度
"""

# 导入模块
import ibbie_14_函数
import ibbie_03_变量

# 调用其它模块的函数
ibbie_14_函数.print_star_heart()
# 调用其它模块的变量
print(ibbie_03_变量.name)
