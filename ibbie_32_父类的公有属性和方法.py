"""
父类的公有属性和方法
    子类可以调用父类的公有属性和方法
    子类对象也可以调用父类的公有属性和方法
    可以通过父类的公有方法，在子类间接调用父类的私有属性和方法
"""


class A:
    def __init__(self):
        self.a = "父类公有属性"
        self.__b = "父类的私有属性"

    def test(self):
        print("父类公有方法")
        print("父类的公有方法中调用父类的私有属性和方法：")
        print(self.__b)
        self.__test2()

    def __test2(self):
        print("父类私有方法")


class B(A):
    def demo(self):
        # 子类调用父类的公有属性和方法
        print(self.a)
        self.test()


b = B()
b.demo()
# 子类对象调用父类的公有属性和方法
print(b.a)
b.test()