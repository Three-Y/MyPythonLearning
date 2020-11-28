"""
__init__()
    创建类的对象时，为对象分配完内存后，会自动执行初始化方法
    可以在初始化方法中使用 self.变量=初始值 添加属性
    如果不想写死属性的值，可以为init方法添加参数，把传递进来的参数赋给属性，创建对象时，要传递对应的参数

__del__()
    当对象被销毁前，会调用del方法
    可以在del中

__str__()
    使用print打印对象时会调用的方法
    默认是打印对象的内存地址
    可以自定义打印对象输出的内容，str方法必须返回一个字符串
"""


class Demo1:

    def __init__(self, name):
        print("我是init，创建对象时会被调用")
        self.a = True
        self.b = 123
        self.name = name

    def __del__(self):
        print("我是del，Demo1对象临死前调用")

    def __str__(self):
        return "我是%s" % self.name


d2 = Demo1("蠢猪")
print(d2.a)
print(d2.b)
print(d2.name)
print(d2)


class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __del__(self):
        print("%s最后的体重是：%.2fkg" % (self.name, self.weight))

    def __str__(self):
        return "%s现在的体重是：%.2fkg" % (self.name, self.weight)

    def eat(self):
        self.weight += 1

    def run(self):
        self.weight -= 0.5


xiaoming = Person("小明", 75.00)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
xiaoming.run()
xiaoming.run()
print(xiaoming)
