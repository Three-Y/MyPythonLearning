"""
列表（list，相当于java中的数组）
    格式：变量名=["hhh","xxx","jjj","aaa"]
    索引值从0开始
    可以存放不同类型的数据，但是通常存放类型相同的数据
"""
"""创建列表"""
name_list = ["hhh", "jjj", "jjj", "aaa"]
print(name_list)

"""根据索引取值"""
name_list[2]
# name_list[4]  # IndexError: list index out of range
print(name_list[2])

"""根据内容取索引"""
name_list.index("aaa")
# name_list.index("111")  # ValueError: '111' is not in list
print(name_list.index("aaa"))

"""修改列表的值"""
name_list[0] = "ibbie"
print(name_list)

"""在末尾添加一个元素"""
name_list.append("yan")
print(name_list)

"""在末尾添加一组元素"""
temp_list = ["1","2","3"]
name_list.extend(temp_list)
print(name_list)

"""在指定索引位置插入元素"""
name_list.insert(3, "doge")
print(name_list)

"""从列表中删除指定的内容"""
name_list.remove("jjj")  # 如果要删除的内容有多个，只删除最前面的一个
print(name_list)

"""pop方法删除元素，pop能返回被删除的元素"""
temp = name_list.pop()  # 不传递参数，默认删除最后一个元素，返回被删除元素
print(temp)
print(name_list)

temp = name_list.pop(1)  # # 传递参数，删除指定索引的元素，返回被删除元素
print(temp)
print(name_list)

"""清空列表"""
name_list.clear()
print(name_list)

"""列表的长度"""
name_list = ["hhh", "jjj", "jjj", "aaa"]
number_list = [7, 2, 2, 2, 10, 6]
print(len(number_list))

"""列表中指定内容的个数"""
print("列表中元素2出现了 %d 次" % number_list.count(2))

"""对列表进行排序"""
name_list.sort()  # 升序排序
number_list.sort()
print(name_list)
print(number_list)

name_list.sort(reverse=True)  # 降序排序，指定reverse为True
number_list.sort(reverse=True)
print(name_list)
print(number_list)

name_list.reverse()  # 反转列表
number_list.reverse()
print(name_list)
print(number_list)

"""迭代列表的元素"""
for name in name_list:
    print("我叫 %s" % name)
