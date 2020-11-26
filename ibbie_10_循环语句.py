"""
程序三大流程
    顺序--从上向下，顺序执行
    分支--根据条件判断，决定执行代码的分支
    循环--让特定代码重复执行

while循环 当满足条件就继续
"""

i = 1  # 计数器初始化
while i <= 10:
    print("hello")
    i = i + 1  # 不要忘记计数器，否则会造成死循环
print("循环结束后，i=%d" % i)  # i=11

# 嵌套循环
m = 1
while m <= 10:
    n = 1
    star = ""
    while n <= m:
        star = star + "*"
        n = n + 1

    print(star)
    m = m + 1

print("----我是一条分隔符----")

# 不换行输出：pring("输出的内容",end="")，默认end是换行符，显式指定end可以改变结尾的符号
j = 10
while j >= 1:
    k = j
    while k >= 1:
        print("⭐", end="♥")  # end=""表示结尾不加任何东西，也可以指定其它符号
        k = k - 1
    print("")
    j = j - 1

print("----我是一条分隔符----")

#  九九乘法表
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print("%d * %d = %d" % (a, b, a * b), end="\t")  # 使用了制表符“\t”
        b = b + 1
    print("")
    a = a + 1
