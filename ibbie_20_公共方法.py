"""
公共方法
    len()       计算容器元素个数
    del()       删除变量
    max()       返回容器中的最大值，如果是字典，只比较key
    min()       返回容器中的最小值，如果是字典，只比较key
    cmp()       比较大小，Python3.X已经取消，可用比较运算符进行比较，但比较运算符不能比较字典
    切片          字符串、列表、元组都支持切片，字典不支持
    *           重复字符串、列表、元组的内容，不会修改原来的内容，字典不支持
    +           合并字符串、列表、元组的内容，不会修改原来的内容，字典不支持
    in & not in 判断是否包含，字典只判断key


    +与append()与extend()的区别
        +           不修改容器原来的内容
        append()    将参数中的内容作为一个元素放到容器中
        extend()    将参数的内容与原容器拼接
"""
t_list = [5, 8, 7, 6, 3]
t_tuple = ("a", 256, 2.5, False, "lalal")
t_dic = {"key1": 12,
         "key2": 200,
         "key3": 10.0}
t_str = "alkndglgahdlhgasdgasz"

"""del关键字 & del()"""
print(t_list)
del t_list[1]
print(t_list)
del(t_list[1])
print(t_list)

"""len()"""
ll = len(t_list)
lt = len(t_tuple)
ld = len(t_dic)
ls = len(t_str)

"""max()"""
ml = max(t_list)
# mt = max(t_tuple)  # TypeError: '>' not supported between instances of 'int' and 'str'
md = max(t_dic)
ms = max(t_str)

"""min()"""
ml = min(t_list)
# mt = min(t_tuple)  # TypeError: '>' not supported between instances of 'int' and 'str'
md = min(t_dic)
ms = min(t_str)

"""切片"""
t_list = [5, 8, 7, 6, 3]
t_tuple = ("a", 256, 2.5, False, "lalal")
print(t_list[2:-1])
print(t_tuple[1:-1:2])

"""重复"""
print(t_list * 2)
print(t_tuple * 5)

"""合并"""
t_list2 = [1, 2]
t_tuple2 = ("haha", 12.3, True)
print(t_list + t_list2)
print(t_tuple + t_tuple2)

"""in & not in"""
print(1 in t_list)
print(256 not in t_tuple)
print("key1" in t_dic)
