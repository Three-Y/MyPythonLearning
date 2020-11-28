"""
父类的私有属性和方法
    虽然子类拥有父类的所有属性和方法，但是子类不能直接调用父类的私有属性和方法
"""


class A:
    def __int__(self):
        self.__a = 123  # 私有属性

    def __test(self):  # 私有方法
        print("我是A的私有方法")


class B(A):
    def demo(self):
        print("我是B的demo()")
        # print(self.a)  # 若调用demo方法，AttributeError: 'B' object has no attribute 'a'
        # super().__test()  # 若调用demo方法，AttributeError: 'super' object has no attribute '_B__test'


b = B()
b.demo()