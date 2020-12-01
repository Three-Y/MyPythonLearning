"""
类属性（类似java的静态属性，但不完全相同）
    类名.类属性
    对象.类属性（不推荐，容易混淆，造成误解）
    若使用 对象.类属性=值 进行赋值操作，只会给对象增加属性，而不会修改类属性
"""


class Demo:
    count = 0  # 记录创建了多少个对象

    def __init__(self):
        # 每创建一个对象count+1
        Demo.count += 1


d1=Demo()
d2=Demo()
d3=Demo()
d4=Demo()
d5=Demo()
print(Demo.count)  # 5
d5.count += 1  # 尝试使用对象修改类属性
print(Demo.count)  # 5 类属性不变
print(d5.count)  # 6 对象属性

"""两个count不是同一个东西"""
print(id(d5.count))  # 1632908634576
print(id(Demo.count))  # 1632908634544
