"""
函数的变量
    在函数内部，对传递进来的参数进行赋值操作，无论是否是可变数据类型，都不会修改函数外部的变量
    对于可变数据类型，在函数内部使用方法进行修改，修改效果能作用到函数外

关于列表的+=操作
    对list使用+=，本质上是执行extend方法：list.extend(list)

函数缺省参数的默认值
    可以在函数的参数列表，对参数设置默认值，如果没有传递对应的参数，直接使用参数的默认值
    设置了默认值的参数（也就是可以缺省的参数），必须放在参数列表的末尾
    如果有多个参数设置了默认值，调用函数时，如果想对指定参数赋值，要加上参数名称

多值参数
    参数名前加*，表示参数是元组，一般习惯元组参数表示成 **args
    参数名前加**，表示参数是字典，一般习惯将字典参数表示成 **kwargs
    不加*也可以对函数传递元组，但调用时需要给参数加上()，而函数参数加了*则可以省略()
    元组和字典的拆包：
        给函数的参数加上*或**后，调用时无需给参数加上()或{}，简化了函数的调用，称为拆包
"""
gl_num = 99
gl_num_list = [1, 2, 3]


def demo1(num, num_list):
    """使用赋值操作修改传递进来的参数（可变+不可变）"""
    print("demo1内，修改前：")
    print(num)
    print(num_list)
    num = 10
    num_list = [4, 5, 6]
    print("demo1内，修改后：")
    print(num)
    print(num_list)


demo1(gl_num, gl_num_list)
print("修改后，函数外部：")
print(gl_num)
print(gl_num_list)


def demo2(num_list):
    """使用方法修改传递进来的参数（可变数据类型）"""
    print("demo2内，修改前：")
    print(num_list)
    num_list.append(666)
    print("demo2内，修改后：")
    print(num_list)


demo2(gl_num_list)
print("修改后，函数外：")
print(gl_num_list)


def demo3(num_list):
    """使用+=运算符"""
    print("在demo3内，使用+=前：")
    print(num_list)
    num_list += num_list
    print("在demo3内，使用+=后：")
    print(num_list)


demo3(gl_num_list)
print("使用+=后，函数外部：")
print(gl_num_list)  # 函数外部list也发生了变化，说明+=运算符执行的不是list = list + list的赋值操作


def demo4(name, is_rich=True):
    """给参数设置默认值，设置了默认值的参数可以缺省"""
    if is_rich:
        answer = "必须的!"
    else:
        answer = "恐怕要再努力点~"
    print("%s会变成有钱人吗？%s" % (name, answer))


demo4("ibbie")
demo4("傻猪猪", False)


def demo5(name, title="打工人", is_hard=True):
    """给多个参数设置默认值"""
    if is_hard:
        answer = "很努力!"
    else:
        answer = "恐怕要再努力点~"
    print("%s是个%s，会变成有钱人吗？%s" % (name, title, answer))


demo5("小明", is_hard=False)  # 跳过title，给is_hard参数赋值，需要带上参数名


def demo6(num, *args, **kwargs):
    """多值参数"""
    print(num)
    print(args)
    print(kwargs)


demo6(1, 2, 3, 4, 5, name="ibbie", gender=False)
# 1分给了num参数，其它数字给了args，键值对给了kwargs
# 1
# (2, 3, 4, 5)
# {'name': 'ibbie', 'gender': False}


def demo7(args):
    temp_total = 0
    for i in args:
        temp_total = temp_total + i

    return temp_total


# TypeError: demo7() takes 1 positional argument but 4 were given
# 函数的参数没有*，解释器会把调用处的参数当成多个个独立的参数，而不是一个元组参数
# 需要给参数加上()
# total = demo7(1, 2, 3, 4)
total = demo7((1, 2, 3, 4))
print(total)
