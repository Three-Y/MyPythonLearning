"""
比较运算符
    == 相等
    != 不等于
    >  大于
    <  小于
    >= 大于等于
    <= 小于等于
"""

"""
逻辑运算符
    and : 条件1 and 条件2
    or : 条件1 or 条件2
    not : not 条件
"""
# if语句
# if语句后缩进的内容都属于if符合条件后要执行的代码块中，没有缩进的部分则离开了if中的代码块，else同理

age = 50

# if
if age < 25:
    print("你太幸福啦！")
    print("哈哈哈哈")
print("啦啦啦啦")  # 无论是否满足条件，此行都会执行

sex = "girl"

# if-else
if sex == "girl":
    print("你是个可爱的女生")
else:  # else必须与if搭配使用
    print("你是个帅气的男生")

# if-elif
if age < 18:
    print("你真可爱")
elif age < 25:
    print("你真漂亮")
elif age < 40:
    print("你真优雅")
else:
    print("你永远18岁")

# if的嵌套
if sex == "girl":
    print("你是个女生")
    if age <= 18:
        print("你最漂亮")
    else:
        print("你永远18岁")
else:
    print("你是个男生")
    print("你是永远的大猪蹄子")
