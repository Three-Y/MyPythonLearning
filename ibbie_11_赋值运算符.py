"""
赋值运算符
    =       a = b + c
    +=      a += b 表示 a = a + b
    -=      a -= b 表示 a = a - b
    *=      a *= b 表示 a = a * b
    /=      a /= b 表示 a = a / b
    //=     a //= b 表示 a = a // b (//表示整除)
    %=      a %= b 表示 a = a % b
    **=     a **= b 表示 a = a ** b
"""
i = 1
total = 0
while i <= 100:
    total += i
    i += 1

print("1到100所有整数的和是：%d" % total)

j = 1
total1 = 0
while j <= 100:
    if j % 2 == 0:
        total1 += j

    j += 1

print("1到100所有偶数的和是：%d" % total1)
