# 函数初体验
def my_len(data):
    count = 0
    for x in data:
        count += 1
    print(f"说了{count}个字")


my_len("Olah! Muhe mimi, nye, eh…mosi aba")


# 函数基础定义
def say_hi():
    print("Olah!")


say_hi()


# 函数的传入参数
def my_calculate(x, y, z):
    """
    三数相加
    :param x:第一个数
    :param y:第二个数
    :param z:第三个数
    :return:相加结果
    """
    print(f"{x}+{y}+{z}={x + y + z}")


my_calculate(0, 30, 648)


# 函数的返回值
def attack_slime(num):
    if num > 58:
        return True


if attack_slime(int(input("输入伤害"))):
    print("战胜史莱姆")
else:
    print("失败")


# 函数嵌套调用
def attack_slimes():
    count = 5
    if attack_slime(int(input("输入伤害"))):
        count -= 1
        print(f"处理一个，还剩{count}只史莱姆")
    else:
        print("失败")


attack_slimes()


# 变量作用域
def creat_weapon():
    global weapon
    weapon = 78


creat_weapon()
if attack_slime(weapon):
    print("武器创建成功")
