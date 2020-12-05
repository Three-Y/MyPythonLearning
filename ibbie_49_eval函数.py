"""
eval函数
    可以将传入的字符串当成有效的表达式进行计算

注意：不要让eval直接接收input的内容，否则用户可以利用__import__('os').system('xxx命令')的方式，执行终端命令
"""

str = input("请输入表达式：")
print(eval(str))
