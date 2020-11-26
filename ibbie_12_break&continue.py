"""
break关键字
    某一条件满足时，退出循环，不再执行后面的循环
continue关键字
    某一条件满足时，退出此次循环，进入下一次循环
    使用continue前要记得考虑，是否需要修改计数器，否则容易进入死循环

break和continue只对当前循环有效
"""
print("**********break***********")
i = 0
while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1

print("**********continue***********")
j = 0
while j <= 10:
    if j == 5:
        j += 1  # 不要忘记修改计数器，否则进入死循环
        continue

    print(j)
    j += 1
