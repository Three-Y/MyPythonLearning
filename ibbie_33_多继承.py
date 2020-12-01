"""
多继承
    一个类继承多个父类，该类拥有所有父类的属性和方法
    如果多个父类中有同名方法，会调用继承类列表中，先定义的那个类的方法（要尽量避免这种情况）
    也要尽量避免使用多继承
"""


class A:
    def __init__(self):
        self.a = "A类的属性"

    def method_a(self):
        print("A类的方法")

    def same_name_method(self):
        print("A类的same_name_method()")

class B:
    def __init__(self):
        self.b = "B类的属性"

    def method_b(self):
        print("B类的方法")

    def same_name_method(self):
        print("B类的same_name_method()")

# class C(B, A):
class C(A, B):
    """C类继承A类和B类，用逗号分隔"""
    pass


c = C()
c.method_a()
c.method_b()
# print(c.a)  # 如果C类的定义是：class C(B, A): 此处会error，AttributeError: 'C' object has no attribute 'a'
# print(c.b)  # 如果C类的定义是：class C(A, B): 此处会error，AttributeError: 'C' object has no attribute 'b'

"""两个父类都有的方法"""
# 如果C类的定义是：class C(B, A): 输出：B类的same_name_method()
# 如果C类的定义是：class C(A, B): 输出：A类的same_name_method()
c.same_name_method()
