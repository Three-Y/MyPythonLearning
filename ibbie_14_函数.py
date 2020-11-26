"""
函数：具有独立功能的代码块，需要时调用

格式：
    def 函数名(参数列表):
        函数体
        return 返回值
"""

# 定义函数 函数定义的上方建议保留两行空行
def print_star_heart():
    """
    此处是print_stat_heart的文档注释
    在调用处使用快捷键ctrl+Q可以查看函数的文档注释
    """
    j = 10
    while j >= 1:
        k = j
        while k >= 1:
            print("⭐", end="♥")  # end=""表示结尾不加任何东西，也可以指定其它符号
            k = k - 1
        print("")
        j = j - 1


# 调用函数
# 调用必须在定义函数之后
print_star_heart()


# 定义带参的函数
def sum_of(num1, num2):
    print("%d + %d = %d" % (num1, num2, num1 + num2))


# 调用带参的函数
sum_of(10, 100)


# 有返回值的函数
def sum_of_2(num1, num2):
    return num1 + num2


# 调用有返回值的函数，接收函数的返回值
result = sum_of_2(100, 500)


# 函数的嵌套调用
def test():
    print("**********我是test()的开始**********")
    print_star_heart()
    sum_of(1,1)
    print("**********我是test()的结尾**********")


test()


# 多个返回值的函数
def test2():
    print("我是test2()")
    # 可以使用元组返回多个数据
    return 1, "haha", {"key1": 666}  # 如果返回的类型是元组，可以省略括号


test2_tuple = test2()
print(test2_tuple)
print(test2_tuple[0])
print(test2_tuple[1])  # 使用下标取值不方便

# 如果需要接收多个返回值，同时需要单独处理每个返回值，可以使用多个变量接收返回值
# 注意：变量的个数必须与返回值的个数一致
num, str2, dic = test2()
print(num)
print(str2)
print(dic)
