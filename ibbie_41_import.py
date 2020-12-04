import ibbie_37_类属性  # 导入模块
import ibbie_39_类方法和静态方法 as ibbie39  # 导入模块并为模块起别名，方便后续调用
from ibbie_40_异常 import input_psw  # 导入模块中指定的工具
from ibbie_14_函数 import *  # （不推荐使用）表示导入模块的全部工具，但是后续调用无需带上模块名
import ibbie_42_内置属性name

"""
注意：假如使用from import导入不同模块的同名工具，后导入的会覆盖前面导入的
可以使用 as 起别名，加以区分
"""

"""
注意：import导入模块时，会将模块中的直接可执行的代码也执行一遍
可以使用__name__属性，加入适当的判断，使代码不会被执行，详见：ibbie_42_内置属性name
"""

# 使用 “模块名.” 调用模块的工具
ibbie_37_类属性.Demo()
# 使用模块的别名调用模块的工具
ibbie39.Tool()
# 使用from xxx import xxx的工具可以直接调用
input_psw()
test2()

