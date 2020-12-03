"""
异常
    try:
        不确定能否正确执行的代码
    except (异常1, 异常2):
        若出现错误需要执行的代码
    except Exception as 变量名:
        对未知错误的处理
    else:
        没有异常才会执行的代码
    finally:
        无论是否发生异常都会执行的代码

    预判程序可能出现的异常，进行适当的处理，提高程序的健壮性
    可以获取捕获的异常==>except Exception as 变量名:

异常的传递
    发生异常后，如果不进行处理，会抛给调用方，调用方不处理，会继续抛给调用方的调用方，以此类推，如果异常抛到主程序都没有被处理，程序终止
"""
"""处理异常"""
try:
    num = int(input("请输入整数："))
except:
    print("你的输入有误！")

print("*" * 20)

"""根据异常类型进行不同的处理"""
try:
    x = int(input("请输入除数："))
    result = 666 / x
    print("666/%d" % x)
except ValueError:
    print("你的输入有误！")
except ZeroDivisionError:
    print("除数不能为0！")

"""获取异常"""
try:
    x = int(input("请输入除数："))
    result = 666 / x
    print("666/%d" % x)
except ValueError:
    print("你的输入有误！")
except Exception as result:
    print(result)

"""else和finally"""
try:
    x = int(input("请输入除数："))
    result = 666 / x
    print("666/%d=%d" % (x, result))
except ValueError:
    print("你的输入有误！")
except Exception as result:
    print(result)
else:
    print("没有异常发生")
finally:
    print("无论是否有异常都会执行")

"""异常的传递"""
def demo1():
    return int(input("请输入除数："))

def demo2():
    b = demo1()
    print("666/%d=%d" % (b, 666 / b))

try:
    demo2()
except Exception as e:
    print("未知异常：%s" % e)
