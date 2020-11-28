"""
私有属性和方法
    在属性名或方法名前添加两条下划线，表示此属性或方法是私有的
    只能在类的内部直接调用
    在python中没有真正的私有属性或方法
    在外部想要调用私有属性或方法，使用 _类名__属性名 或 _类名__方法名 的方式调用（不建议使用）
"""


class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    def getname(self):
        self.__getage()  # 类内部可以调用私有方法
        print("我叫%s今年%d岁" % (self.name, self.__age))  # 类内部可以调用私有属性

    def __getage(self):  # 私有方法
        print("我今年%d岁" % self.__age)


d = Girl("猪猪girl")
# d.__age  # AttributeError: 'Girl' object has no attribute '__age'
print(d._Girl__age)  # _类名__私有属性 可以在类外部调用私有属性
d._Girl__getage()  # _类名__私有方法 可以在类外部调用私有方法
# d.__getage()  # AttributeError: 'Girl' object has no attribute '__getage'
d.getname()
