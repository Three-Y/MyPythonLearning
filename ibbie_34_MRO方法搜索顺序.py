"""
MRO方法搜索顺序
    类名.__mro__  可以调用python提供的内置属性mro查看方法的调用顺序
    python查找方法的顺序是：本类==>父类（按声明顺序从左到右）==>Object类（python所有类的基类）
"""


class Test:
    pass


print(Test.__mro__)
