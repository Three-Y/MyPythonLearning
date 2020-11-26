"""
面向对象
    dir()可以查看python针对该对象提供的内置的方法或属性

定义类的格式：
    class 类名:
        def 方法名1(self, 参数列表):
            pass
        def 方法名2(self, 参数列表):
            pass

创建类的对象
    变量名 = 类名()
    不修改类，可以使用 变量名.属性 为对象增加属性（不推荐）

关于类的定义：
    使用class关键字
    定义方法的第一个参数必须是self

关于self
    表示对象本身，可以使用self在类中调用属性或方法，包括使用 变量名.属性 增加的属性，也可以使用self调用
"""


def demo():
    """我是demo"""
    print("我是demo")


print(dir(demo))
print(demo.__doc__)
print(dir("abc"))
print(dir(2))
print(dir(True))



"""定义一个类"""
class DemoClass:

    def method1(self, num):
        print("method1")

    def method2(self, a, b, c):
        print("method2")

"""创建类的对象"""
d = DemoClass()
d.method1(1)
d.method2(1, 2, 3)
print(d)  # <__main__.DemoClass object at 0x00000219B4288FD0>
print("%x" % id(d))  # 219b4288fd0
d.name = "hahah"
print(d.name)
