"""
ASCII编码
    早期使用的编码，只有256个字符，每个字符占1字节
UNICODE编码
    几乎涵盖了全世界所有的字符
    UTF-8,是UNICODE的一种
        使用1-6个字节表示一个字符
        大多数汉字使用3个字节表示

Python2.X默认使用ASCII
Python3.X默认使用UTF-8

可以在文件开头指定编码
    添加注释：# *-* coding:utf8 *-*
    或：# coding=utf8

python2.X会将中文字符切成3个1个字节的字符输出，就会导致乱码
    可以在字符串前加一个u，表示这是一个utf-8编码的字符串
"""

str = u"我是一条字符串"

for c in str:
    print(c)