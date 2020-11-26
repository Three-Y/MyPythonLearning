"""
元组（tuple）
    与列表类似，但是元组定义完成后，不能修改
    用()定义
    索引从0开始
    通常存放不同类型的数据

应用场景：
    作为函数的参数或返回值，使得函数可以接收多个参数，或者返回多个返回值
    格式化字符串
    让列表不能被修改，保护数据安全
"""

"""元组的定义"""
person_tuple = ("张三", 20, 1.75)

empty_tuple = ()  # 空元组

single_tuple = (1)  # 这不是一个元组
print(type(single_tuple))  # <class 'int'>
single_tuple = (1,)  # 只有一个元素的元组，元素后面要加上","
print(type(single_tuple))  # <class 'tuple'>

"""取值或取索引"""
print(person_tuple[0])
# person_tuple[3]  # IndexError: tuple index out of range
print(person_tuple.index(20))
# print(person_tuple.index(21))  # ValueError: tuple.index(x): x not in tuple

"""元组的长度"""
print(len(person_tuple))

"""元组中指定内容的个数"""
print(person_tuple.count(1.75))

"""遍历元组"""
for temp in person_tuple:
    print("%s : %s" % (type(temp), temp))

"""格式化字符串"""
print("%s 的年龄是 %d ，身高 %.2f m" % person_tuple)
person_str = "%s 的年龄是 %d ，身高 %.2f m" % person_tuple
print(person_str)

"""list和tuple之间的转换"""
person_list = list(person_tuple)  # 元组==>列表
print(type(person_list))  # <class 'list'>

temp_tuple = tuple(person_list)  # 列表==>元组
print(type(temp_tuple))  # <class 'tuple'>
