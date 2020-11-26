"""
for循环

    for temp in 容器:
        某些操作
    else:
        某些操作

执行完循环体后，才会执行else的内容，如果循环中途使用break退出循环，则不会执行else的内容
一般情况下不会加上else，常用于搜索操作，若搜索不到则执行else的内容
"""
t_list = [1, 2, 3]
for num in t_list:
    print(num)
    if num == 2:
        break
else:
    print("结束")

student_list = [{"name": "小明",
                 "age": 20},
                {"name": "小红",
                 "age": 21},
                {"name": "小白",
                 "age": 22}]

stu = "ibbie"
for stu_dic in student_list:
    if stu_dic["name"]==stu:
        print(stu_dic)
        print("找到"+stu+"了")
        break
else:
    print("找不到"+stu)
