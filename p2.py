slime = 58
hilichurl = 73
attack = 60

# 布尔类型
ret = slime == hilichurl
print(f"slime == hilichurl结果：{ret},类型是：{type(ret)}")

# if语句
if attack > slime:
    print("消灭了史莱姆")
print("还不够")

# if else 组合
damage = int(input("输入伤害："))
if damage > slime:
    print("战胜史莱姆")
else:
    print("还不够")

# elif 使用
damage = int(input("再次输入伤害"))
if damage > hilichurl:
    print("战胜丘丘人")
elif damage > slime:
    print("战胜史莱姆")
else:
    print("还不够")

# 判断语句嵌套
if int(input("1打死士，2打崩坏兽")) == 1:
    if int(input("1选机械，2选异能")) == 1:
        print("克制死士")
    else:
        print("被死士克制")
else:
    if int(input("1选生物，2选机械")) == 1:
        print("克制崩坏兽")
    else:
        print("被崩坏兽克制")
