"""
多态
    不同的子类对象，调用相同的父类方法，产生不同的结果（同java，略）
"""


class Animal:
    def eat(self):
        print("吃东西")


class Dog(Animal):
    def eat(self):
        print("狗狗吃骨头")


class Cat(Animal):
    def eat(self):
        print("猫猫吃鱼")


class Master:
    def feed(self,animal):
        animal.eat()


cat = Cat()
dog = Dog()
master = Master()
master.feed(cat)
master.feed(dog)
