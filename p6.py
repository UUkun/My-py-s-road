# 函数多个返回值
def my_weapon():
    return 'dull', 23, 185


x, y, z = my_weapon()
print(x)
print(y)
print(z)


# 多种传参方式
def weapon_info(name, atk, quality=4):
    print(f"名字是{name}，攻击是{atk}，稀有度是{quality}")


# 位置参数-默认
weapon_info('dull', 23, 1)
# 关键字传参
weapon_info(atk=33, name='silver', quality=2)
# 缺省参数
weapon_info('flute', 42)


# 不定长参数-位置不定长
def enemy_info(*args):
    print(f"敌人是：{args}, 类型是{type(args)}")


enemy_info('hilichurl', 73, 46)


# 关键字不定长
def fish_info(**kwargs):
    print(f"鱼是：{kwargs}，类型是{type(kwargs)}")


fish_info(name='raimei', quality=3, dificulty='vhard')


# 函数作为参数
# 定义函数，接受另一个函数
def do_some(do):
    result = do(73, 23)
    print(f"do的类型是：{type(do)}")
    print(f"作用结果是：{result}")


# 定义函数，作为参数传递
def attack(hp, atk):
    return hp - atk


# 调用，传入函数
do_some(attack)

# lambda匿名函数作为参数
do_some(lambda hp, atk: hp - atk)
