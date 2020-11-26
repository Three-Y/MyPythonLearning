"""
格式化字符
    %s 字符串
    %d 有符号的十进制整数，%06d表示显示6位数，不足补0
    %f 浮点数，%.2f表示保留两位小数
    %% 输出%
    %x 以十六进制的方式输出

print("格式化字符串" % 变量1)
print("格式化字符串" % (变量1,变量2,变量3...))
"""
name = "ibbie"
print("我叫%s" % name)  # 我叫ibbie

stu_no = 123
print("我的学号是%06d" % stu_no)

price = 2.5
weight = 5
money = price * weight
print("苹果的单价是%.2f/斤，一共%.2f斤，需要支付%.2f元" % (price, weight, money))

scale = 0.9999
print("你暴富的概率是%.2f%%" % (scale * 100))  # 注意，若计算部分不加括号，会将字符串输出100遍