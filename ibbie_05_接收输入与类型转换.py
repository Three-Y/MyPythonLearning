# input()函数
input()

# 显示输入信息，并将接收的数据赋给变量
# input()的返回值是字符串
price = input("请输入单价：")
count = input("请输入个数：")
# print("总价是："+price*count)  # TypeError: can't multiply sequence by non-int of type 'str'
# 需要进行类型转换才能进行计算

# 类型转换
a = int("123")
b = float("123")
