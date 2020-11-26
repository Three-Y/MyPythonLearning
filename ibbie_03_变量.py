# 变量名 = 变量值
a = "123"
print(a)

m = 1
n = 2
mn = m*n
mn = mn + 10
print(mn)

"""
python中不需要声明变量类型
会自动根据右边的数据推导出准确的类型
在交互式运行中，可以使用type()可以查看某变量具体类型
"""
name = "ibbie"  # str
age = 1  # int
gender = False  # bool
high = 1.58  # float
weight = 95.0  # float,若不加".0"会是int

"""
数据类型

数值型 ：数值型之间可以相互进行运算
    整型 int :在python2.x的时候还分int和long，python3.x后只有int
    浮点型 float
    布尔型 bool :若布尔型参与运算，true代表1，false代表0
        True 非0数
        False 0
    复数型 complex 主要用于科学计算

非数值型
    字符串
    列表
    元组
    字典
"""