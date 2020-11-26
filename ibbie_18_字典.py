"""
字典（dictionary）
    使用键值对存储数据，通常用于存储描述一个物体的相关信息
    字典是一个无序的数字集合
    字典名 = {键:值,键:值,键:值,键:值}
    键是唯一的，只使用字符串、数字或元组
    值可以是任何类型，一个键对应只有一个值
"""

"""定义字典"""
ibbie_dic = {"name": "ibbie",
             "age": 1,
             "height": 2.00,
             "hobby": "敲代码"}
print(ibbie_dic)

"""从字典中取值"""
print(ibbie_dic["name"])
# ibbie_dic["gender"]  # 若key不存在，报错：KeyError

"""根据key修改value，若key不存在，会在字典中添加新的键值对"""
ibbie_dic["age"] = 2  # key存在，修改key对应的value
print(ibbie_dic)

ibbie_dic["weight"] = 90.0  # key不存在，新增键值对
print(ibbie_dic)

"""删除键值对"""
ibbie_dic.pop("age")
print(ibbie_dic)
# ibbie_dic.pop("abc")  # KeyError

"""字典中键值对的数量"""
print(len(ibbie_dic))

"""合并字典"""
temp_dic = {"phone": "13100000000",
            "gender": False}
ibbie_dic.update(temp_dic)
print(ibbie_dic)

temp2_dic = {"phone": "13188888888"}
ibbie_dic.update(temp2_dic)  # 如果合并的字典中有相同的key，会替换掉被updated的字典中相同key的value
print(ibbie_dic)

"""清空字典"""
ibbie_dic.clear()
print(ibbie_dic)

"""遍历字典"""
ibbie_dic = {"name": "ibbie",
             "age": 1,
             "height": 2.00,
             "hobby": "敲代码"}
for k in ibbie_dic:
    print("%s : %s" % (k, ibbie_dic[k]))
