"""
导入包
"""

import ibbie_43_package

ibbie_43_package.test_package.test43()
"""
因为ibbie_43_package的__init__.py中没有声明这个模块，所以无法调用
Cannot find reference 'test_package2' in '__init__.py' 
"""
# ibbie_43_package.test_package2.test43_2()