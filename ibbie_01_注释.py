# 我是注释，建议“#”后面加一个空格
print("我是程序")

print("啦啦啦")  # 在代码后注释，建议代码与“#”之间有两个空格

"""
多行注释
多行注释
多行注释
"""
print("hhh")


# 快捷键shift+alt+F调整代码格式


# 文档注释
def function(a, b):
    """
    此处是函数的文档注释
    在调用处使用快捷键ctrl+Q可以查看函数的文档注释

    :param  a:我是a参数的文档注释
    :param  b:我是b参数的文档注释
    :return 我是返回值的文档注释
    """
    print("执行函数function")
    return a + b


function(1, 1)
