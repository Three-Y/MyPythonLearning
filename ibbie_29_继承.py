"""
继承
    子类继承父类所有的方法和属性
    继承的格式：
        class 类名(父类名):
            pass

    可以多重继承，C继承B，B继承A，C也具有A的属性和方法
"""


class Animal:

    def eat(self):
        print("吃东西")

    def sleep(self):
        print("睡觉")


class Dog(Animal):

    def bark(self):
        print("汪汪汪")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class HelloKitty(Cat):
    def cute(self):
        print("可可爱爱")


dog = Dog()
dog.eat()  # Animal类的方法
dog.sleep()  # Animal类的方法
dog.bark()  # Dog自己的方法

hk = HelloKitty()
hk.eat()  # Animal类的方法
hk.cute()  # Animal类的方法
hk.catch()  # Cat类的方法
hk.sleep()  # HelloKitty自己的方法
