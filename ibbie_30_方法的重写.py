"""
方法的重写
    父类的方法不能满足子类的需求
    在子类中定义与父类同名的方法，重写方法的实现即可

super()
    代表父类
    可以通过super()调用父类的方法，super().方法名()
    重写方法时，可以通过调用父类的方法，不完全覆盖父类的方法，实现方法的扩展
"""


class Animal:

    def eat(self):
        print("吃东西")

    def sleep(self):
        print("睡觉")


class Dog(Animal):

    def bark(self):
        print("汪汪汪")

    def sleep(self):  # 重写父类的方法
        print("四脚朝天地睡")

    def eat(self):
        super().eat()  # 调用父类的eat方法
        print("吃的是骨头")


dog = Dog()
dog.sleep()  # 调用的是Dog重写的sleep方法
dog.eat()
dog.bark()
