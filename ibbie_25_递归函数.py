"""
递归函数
    自己调用自己
    要有出口条件
"""


def sum_num(num):
    """计算从1到num所有整数的和"""
    if num == 1:  # 出口条件，没有出口条件会死循环
        return 1
    else:
        return num + sum_num(num - 1)  # 自己调用自己


total = sum_num(20)
print(total)