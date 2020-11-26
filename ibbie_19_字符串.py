"""
字符串
    可以用双引号或单引号定义字符串，一般使用双引号
    str = "abc"
    假如字符串中包含双引号，则使用单引号来定义
    str = 'lalala"啦啦啦"'
    可以帮字符串看成是一个列表，列表的每个元素都是一个字符
    字符串的索引值从0开始
"""

"""定义字符串"""
str1 = "abc"
print(str1)
str2 = '"哈哈"'
print(str2)

"""遍历字符串"""
str3 = "abc123321cba"
for char in str3:
    print(char)

"""字符串的长度"""
print(len(str3))

"""统计子字符串在字符串中出现的次数"""
print(str3.count("a"))
print(str3.count("z"))  # 没有则返回0

"""从字符串中查找，并返回索引值"""
idx = str3.index("123")
print(idx)  # 返回的是查找的字符串的第一个字符在字符串中的索引
# idx2 = str3.index("1234")  # 若查找的小字符串不存在，报错：ValueError: substring not found

"""***********字符串常用方法***********"""

"""是否只有空白字符"""
empty_str = ""
space_str = "   "
print(empty_str.isspace())  # False
print(space_str.isspace())  # True

"""是否只包含数字"""
num_str = "一百一十一"
print(num_str.isdecimal())  # 12.3(×)  123(√)  ①(×)  一百一十一(×)
print(num_str.isdigit())  # 12.3(×)  123(√)  ①(√)  一百一十一(×)
print(num_str.isnumeric())  # 12.3(×)  123(√)  ①(√)  一百一十一(√)

"""查找与替换"""
hello_str = "hello world"
print(hello_str.startswith("HELLO"))  # False  是否以某字符串开头
print(hello_str.endswith("world"))  # True  是否以某字符串结尾

print(hello_str.find("llo"))  # 2  查找字符串，返回索引值
print(hello_str.find("abc"))  # -1  与index不同，找不到也不会报错，会返回-1

print(hello_str.replace("world", "python"))  # hello python  替换指定内容，返回替换后的新字符串
print(hello_str)  # hello world  但是旧字符串不会被改动

"""文本对齐"""
poem = ["题目",
        "作者",
        "我是第一行诗",
        "我是第二行诗",
        "我是第三行诗",
        "我是第四行诗", ]
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "🍔"))  # 居中
    # print("|%s|" % poem_str.center(10,"**"))
    # 填充的字符只能是一个字符，否则报错：TypeError: The fill character must be exactly one character long

for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "🍟"))  # 左对齐

for poem_str in poem:
    print("|%s|" % poem_str.rjust(10, "🍖"))  # 右对齐

"""去除空白字符"""
space_str = "  ab|  |cdef  "
print(space_str.lstrip())  # 去除左边的空白字符
print(space_str.rstrip())  # 去除右边的空白字符
print(space_str.strip())  # 去除两边的空白字符

"""拆分和连接"""
split_str = "abc*efg*jjj* kkk*ooo"
sp1 = split_str.split()
sp2 = split_str.split("*")
print(sp1)  # 分割字符，默认以空白字符分割,返回一个list
print(sp1)  # 分割字符，按指定字符分割，返回一个list2

print("🚗".join(sp2))  # 连接字符串，用指定字符连接

"""
截取字符串
    字符串有两种索引的方式
        正序 从第一个字符开始往后：0，1，2，3...
        倒序 从最后一个字符开始往前：-1,-2,-3...
    语法：
        string[开始索引:结束索引:步长]
        开始索引的字符包含在要截取的字符串中
        结束索引的字符不包含在要截取的字符串中
        步长为整数，从左往右走，步长为负数，从右往左走
"""
str4 = "012345678"
print(str4[2:5])  # 234 截取索引2到4的字符
print(str4[3:])  # 345678 截取索引3到末尾
print(str4[:6])  # 012345 截取开头到索引5
print(str4[::2])  # 02468 从头到尾，每隔一个取一个字符
print(str4[1::2])  # 1357 从索引1开始，每隔一个取一个字符
print(str4[2:-1])  # 234567 从索引2开始，取到倒数第二个字符
print(str4[-2])  # 7 取倒数第二的字符
print(str4[-2:])  # 78 取最后两个字符
print(str4[-1::-1])  # 876543210 逆序，从最后一个字符开始，步长-1，即每取一个字符向前移动一格
print(str4[::-1])  # 876543210 逆序，步长-1，即每取一个字符向前移动一格
