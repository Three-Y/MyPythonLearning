from distutils.core import setup
"""
一个发布模块的程序
    需要在终端执行，并加上build命令，构建模块
    若发布的模块是针对py2.x，使用python2的解释器（python setup.py build）
    若发布的模块是针对py3.X，使用python3的解释器（python3 setup.py build）
"""
setup(name="test_package_module",  # 包名
      version="1.0",  # 版本号
      description="just test for package module",  # 描述信息
      long_description="测试打包模块",  # 完整描述信息
      author="ibbie.yan",  # 作者
      author_email="913779449@qq.com",  # 作者邮箱
      url="www.ibbie.com",  # 作者网址
      py_modules=["ibbie_43_package.test_package",  # 要打包的模块，放进list中
                  "ibbie_43_package.test_package2"])
