"""
文件操作
    打开 open(文件名,打开方式)
        默认以只读形式打开文件
        f 只读，默认值
        w 只写，若文件存在，覆盖原文件，若文件不存在，自动创建
        a 追加
        r+ 读写，若文件不存在，抛出异常
        w+ 读写，若文件存在，覆盖原文件，若文件不存在，自动创建
        a+ 读写，若文件存在，在文件指针指向末尾追加，若不存在，自动创建
        注意：频繁移动文件指针会影响文件读写效率，所以一般使用无+号的三个参数
    读 read()
    分行读 readline()
    写 write()
    关闭 close()

文件指针
    在使用open()打开文件后，文件指针指向文件开头
    使用read()后，文件指针指向文件结尾，默认读取文件所有内容
    再次调用read()，就没有任何数据可以获取了

import os 文件/文件夹操作的包
    
"""
import os  # 文件/文件夹操作的包

"""打开文件"""
file = open("readme.txt")  # 会在当前目录下寻找

"""读取文件"""
text = file.read()
print(text)
print("*" * 34)
text2 = file.read()
print(text2)  # 没有内容输出
# file.write("try to write")  # 文件是以只读的形式打开的，不能进行写的操作：io.UnsupportedOperation: not writable

"""关闭文件"""
file.close()

"""以追加方式写入文件"""
file = open("readme.txt", "a")
file.write("phone:10086")
file.close()

"""分行读取"""
file = open("readme.txt")

while True:
    text3 = file.readline()
    if not text3:
        break
    print(text3)
file.close()

"""小文件的复制，可以一次读取，一次写入"""
# file1 = open("readme.txt")
# file2 = open("readme[copy].txt","w")  # 只写，文件不存在会自动创建，创建在当前文件夹下
#
# text = file1.read()
# file2.write(text)
#
# file1.close()
# file2.close()

"""大文件的复制，分行读写"""
# file1 = open("readme.txt")
# file2 = open("readme[copy].txt","w")  # 只写，文件不存在会自动创建，创建在当前文件夹下
#
# while True:
#     text = file1.readline()
#     if not text:
#         break
#     file2.write(text)
#
# file1.close()
# file2.close()

"""
文件/文件夹的相关操作
要导入os包
"""

"""重命名文件"""
# os.rename("readme[copy].txt","README[COPY].txt")

"""删除文件"""
# os.remove("README[COPY].txt")

"""查看目录下的内容"""
# dir_list = os.listdir(".")
# print(dir_list)

"""判断是否是文件夹"""
# print(os.path.isdir("ibbie_45_发布模块"))  # True
# print(os.path.isdir("HelloPython.py"))  # False

"""创建与删除目录"""
# os.mkdir("test")  # 若文件夹已存在：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'test'
# os.rmdir("test")  # 若文件夹不存在：FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'test'

"""获取当前目录"""
dir_curr = os.getcwd()
print(dir_curr)
