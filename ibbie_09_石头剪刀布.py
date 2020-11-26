import random

# 玩家
player = int(input("请选择 石头(1)剪刀(2)布(3)："))

# 系统
sys = random.randint(1, 3)
print("系统出的是 石头(1)剪刀(2)布(3)：%d" % sys)

# 比较
if (player == 1 and sys == 2) \
        or (player == 2 and sys == 3) \
        or (player == 3 and sys == 1):
    print("你赢了")
elif player == sys:
    print("平局")
else:
    print("你输了")
