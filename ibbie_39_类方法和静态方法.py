"""
类方法
    @classmethod
    def 类方法名(cls):
        pass

    cls表示当前类
    @classmethod表示这是一个类方法
    类方法的第一个参数必须是cls
    cls.类属性 调用类属性

静态方法
    @staticmethod
    def 静态方法名():
        print("我是静态方法")

    @staticmethod表示这是一个静态方法
    可以将 不需要访问实例属性和类属性 以及 不需要调用实例方法和类方法 的方法定义成静态方法
    类名.静态方法() 调用静态方法
"""


class Tool:
    count = 0

    @classmethod
    def get_tool_count(cls):
        print(cls.count)

    @staticmethod
    def test_methon():
        print("我是静态方法")


Tool.get_tool_count()
Tool.test_methon()
