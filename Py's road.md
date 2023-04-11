# py's road

## my first py

### 你好，世界
优雅的py之路从hello world开始
```python
print('hello world')
```

---

### 简单的注释环节
```python
print('say hi')# print('hello world')
'''
这是大块儿的
注释
'''
```
_讨厌的人有两种：_
* _~~一是代码不写注释的~~_
* _~~二是让我写注释的~~_

---

### 初识变量
```python
# 万恶之源
primogem = 5600
# 花费十连*1
primogem = primogem - 1600
print('花费一个十连，还剩', primogem, '原石')
```
*与变量的相逢总是平淡却不平凡*

---

### 相遇的第一件事
```python
print(type("name"))
print(type(primogem))
print(type(2800.00))
```
*君の名は。*

---

### 神奇的格式变换
```python
# int->str
pri_str = str(primogem)
print(type(pri_str), pri_str)
# str->int
crystals_str = '2800'
cry_int = int(crystals_str)
print(type(cry_int), cry_int)
# float->int
attack = 674.51
atk_int = int(attack)
print(type(atk_int), atk_int)  # 丢失精度
```
*~~百变小樱~~*

---

### 标识符的那些事
```python
# 内容限定
# 1_name = 'kiana'
# name_! = 'bronya'
# 大小写敏感
name = 'Raiden'
Name = 'Mei'
print(name, Name)
# 不可用关键字
# class = 'kaslana'
```
*现在是，我的回合*

---

### （初识）运算符
```python
# 运算符N则
print('648 + 328 =', 648 + 328)
print('648 - 328 =', 648 - 328)
print('648 * 328 =', 648 * 328)
print('9 / 2 =', 9 / 2)
print('9 // 2 =', 9 // 2)
print('9 % 2 =', 9 % 2)
print('9 ** 2 =', 9 ** 2)
```
*犹豫，就会败北*

---

### 面向字符串
```python
# 字符串相关
print("'外双内单'")
print('"外单内双"')
print("\"使用转义\"")
# 字符串合并
# print("base ATK"+ 608) --error
print("base ATK" + "608")
# 使用占位符
print("一共%s，抽了%d，打出了%f" % (primogem, 2800, attack))
# 字符串格式化
print("最终数值 %.0f" % attack)
# 格式化方法2
print(f"你至少应该为她流{attack}滴眼泪")
# 运算符
print("200爆伤，黄字：%.1f" % (attack*2))
# 数据输入
criticalDMG = input("输入爆伤(%)：")
print("暴击，atk：%.1f" % (float(criticalDMG)*0.01*attack))
```
结束p1

---

## yes or no

### 认识布尔
```python
# 布尔类型
ret = slime == hilichurl
print(f"slime == hilichurl结果：{ret},类型是：{type(ret)}")

```

---

### 使用if
```python
# if语句
if attack > slime:
    print("消灭了")
print("还不够")
```

---

### if与else的组合
```python
# if else 组合
damage = int(input("输入伤害："))
if damage > slime:
    print("战胜史莱姆")
else:
    print("还不够")
```

---

### if与elif的连击
```python
damage = int(input("再次输入伤害"))
if damage > hilichurl:
    print("战胜丘丘人")
elif damage > slime:
    print("战胜史莱姆")
else:
    print("还不够")
```

---

### 嵌套QTE
```python
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
```
*俄罗斯套娃*

结束p2

---

## 循环的世界

### 陷入while
```python
# while循环
exp = 0
i = 0
while i < 100:
    i += 1
    exp += i
    print(f"第{i}次练级，经验为{exp}")
```
*无限*

---

### 走进for
```python
# for循环
name = "Lata movo dada"
i = 0
for x in name:
    if x == 'a':
        i += 1
print(f"\"Lata movo dada\"里有{i}个\'a\'")
```

---

### for与嵌套
```python
# for循环嵌套
for i in range(1,8):
    for j in range(1,11):
        print(f"第{i}天的第{j}只丘丘人")
```
*人类的本质*

---

### 跳出循环
```python
# break&continue
for i in range(1,5):
    for j in range(1,3):
        print(f"{j}个丘丘没病")
        if i < 2:
            continue
        print(f"{j}个丘丘病了")
        if i < 4:
            break
        print(f"{j}个丘丘好了")
```
*禁止复读*

结束p3

---

## 与函数的相逢

### 优雅的邂逅
```python
# 函数初体验
def my_len(data):
    count = 0
    for x in data:
        count += 1
    print(f"说了{count}个字")


my_len("Olah! Muhe mimi, nye, eh…mosi aba")
```

---

### 函数入门到
```python
# 函数基础定义
def say_hi():
    print("Olah!")


say_hi()
```
*入土*

---

### 输入
```python
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
```

---

### 输出
```python
# 函数的返回值
def attack_slime(num):
    if num > 58:
        return True


if attack_slime(int(input("输入伤害"))):
    print("战胜史莱姆")
else:
    print("失败")
```
*知道因为啥失败吗♫*

---

### 函数嵌套
```python
# 函数嵌套调用
def attack_slimes():
    count = 5
    if attack_slime(int(input("输入伤害"))):
        count -= 1
        print(f"处理一个，还剩{count}只史莱姆")
    else:
        print("失败")


attack_slimes()
```
*真让我替你感到悲哀♫*

---

### 变量作用域
```python
# 变量作用域
def creat_weapon():
    global weapon
    weapon = 78


creat_weapon()
if attack_slime(weapon):
    print("武器创建成功")
```
结束p4

---

## 与容器的邂逅
### 灵活的列表
```python
# 列表的定义
my_weapon = ['sword', 'claymore', 'polearm']
print(my_weapon, type(my_weapon))

# 列表下标索引
print(my_weapon[0])
print(my_weapon[1])
print(my_weapon[-1])

# 列表的方法
# 查找元素的下标索引 list.index
print(f"claymore的下标索引是{my_weapon.index('claymore')}")
# 修改特定下标的值
my_weapon[1] = 'bow'
print(my_weapon)
# 插入一个元素
my_weapon.insert(1, 'catalyst')
print(my_weapon)
# 尾插一个元素
my_weapon.append('claymore')
print(my_weapon)
# 追加一批元素
my_weapon.extend(['swords', 'claymores'])
print(my_weapon)
# 删除元素
del my_weapon[3]
print(my_weapon)
# 取出元素
weapon = my_weapon.pop(4)
print(f"取出了{weapon}, 还剩下{my_weapon}")
# 删除列表中第一个匹配元素
my_weapon.remove('sword')
print(my_weapon)
# 列表长度
print("列表长度：", len(my_weapon))
# 清空列表
my_weapon.clear()
print("列表清空：", my_weapon)
# 统计元素
enemies = ['slime', 'hilichurl', 'hilichurl', 'hilichurl']
print(f"hilichurl有{enemies.count('hilichurl')}个")
```

---

### 列表的遍历
```python
# 列表遍历
# while循环
index = 0
while index < len(enemies):
    print(enemies[index])
    index += 1
# for循环
for enemy in enemies:
    print(enemy)
```

---

### 关于元组
```python
# 元组
# 定义元组
attribute = (73, "hilichurl", True)
print(f"attribute的类型是{type(attribute)}，内容是{attribute}")
# 定义单个元素元组
single_hili = ("hilichurl",)
print(f"single_hili的类型是{type(single_hili)}，内容是{single_hili}")
# 元组嵌套
e_w = (("hilichurl", "slime"), ("sword", "bow"))
print(f"e_w的类型是{type(e_w)}，内容是{e_w}")
# 下标索引
print(f"e_w[1][0]是{e_w[1][0]}")
# 元组index
print(f"slime在e_w[0]中的位置是{e_w[0].index('slime')}")
# 元组count
enemies_t = ('slime', 'hilichurl', 'hilichurl', 'hilichurl')
print(f"enemies_t中有{enemies_t.count('hilichurl')}个hilichurl")
# 元组while遍历
index = 0
while index < len(enemies_t):
    print(f"元组中有：{enemies_t[index]}")
    index += 1
# 元组for遍历
for ew in e_w:
    print(f"元组e_w里有：{ew}")
# 元组内元素内容修改
weapon_t = (['sword', 'bow'], ['claymore'])
weapon_t[1][0] = 'catalyst'
print(f"weapon[1][0]为{weapon_t[1][0]}")
```

---

### 操作字符串
```python
# 字符串
hili_say = "Biat ye, ye pupu dada mosi! Plama ye upa dada!"
# 通过下标索引
print(f"从字符串{hili_say}中下标为2元素为{hili_say[2]}，下标为-18的元素为{hili_say[-18]}")
# index方法
print(f"在字符串{hili_say}中查找ye，下标为{hili_say.index('ye')}")
# replace方法
new_hili_say = hili_say.replace("dada", "奥里给")
print(f"将字符串{hili_say}替换后，得到：{new_hili_say}")
# split方法
hili_say_list = hili_say.split(" ")
print(f"将字符串{hili_say}split切分后，得到：{hili_say_list}，类型是{type(hili_say_list)}")
# strip方法
new_hili_say = hili_say.strip('!')
print(f"字符串{hili_say}被strip后，为：{new_hili_say}")
# 统计字串出现次数
print(f"字符串{hili_say}中ye出现次数为：{hili_say.count('ye')}")
# 统计字符串长度
print(f"字符串{hili_say}长度为：{len(hili_say)}")
```

---

### 进行切片
```python
# 数据容器切片
# 对list切片
print(f"enemies切片：{enemies[1:3]}")
# 对list切片 步长-1
print(f"enemies切片步长-1：{enemies[::-1]}")
```

---

### 使用集合
```python
# 定义集合
artifact = {"plume", "sands", "goblet", "circlet"}
print(f"artifact集合的内容是：{artifact}，类型是{type(artifact)}")
# 添加新元素
artifact.add('flower')
artifact.add('sands')
print(f"artifact集合的内容是：{artifact}")
# 移除元素
artifact.remove('sands')
print(f"artifact集合的内容是：{artifact}")
# 随机取出元素
print(f"随机取出{artifact.pop()}，取出后：{artifact}")
# 清空集合
artifact.clear()
print(f"artifact集合的内容是：{artifact}")
# 2个集合差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(f"差集结果：{set1.difference(set2)}")
# 消除差集
set1.difference_update(set2)
print(f"消除差集后set1：{set1}")
print(f"消除差集后set2：{set2}")
# 集合合并
set1 = {1, 2, 3}
set3 = set1.union(set2)
print(f"set1和set2合并后：{set3}")
# 统计集合内数量
print(f"set3内数据数量：{len(set3)}")
# for循环遍历集合
for x in set1:
    print(f"{x}")
```

---

### 来到字典
```python
# 定义字典
swords = {"dull": 23, "silver": 33, "skyrider": 38}
print(f"字典内容是：{swords}")
# 从字典基于key获取value
print(f"dull的atk是：{swords['dull']}")
# 嵌套字典
swords_dict = {
    "dull": {
        "baseATK": 23,
        "ATK": 185
    },
    "silver": {
        "baseATK": 33,
        "ATK": 243
    }
}
print(f"sword的信息是：{swords_dict}")
# 从嵌套字典获取信息
print(f"dull的ATK信息：{swords_dict['dull']['ATK']}")
# 新增/更新元素
swords["flute"] = 42
print(f"结果：{swords}")
# 删除元素
print(f"删除dull：{swords.pop('dull')}，还剩：{swords}")
# 获取全部key
print(f"sword的keys：{swords.keys()}")
# 遍历字典
# 1、
for key in swords.keys():
    print(f"swords的key是：{key}")
    print(f"swords的value是：{swords[key]}")
# 2、
for key in swords:
    print(f"swords的key是：{key}")
    print(f"swords的value是：{swords[key]}")
# 统计字典内元素数量
print(f"swords里有{len(swords)}个元素")
```
结束p5

---

## 与函数的重逢
### 函数的多重套路
```python
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
```
结束p6

---

## 浩博的文件
### 品读文件
```python
# 文件的读取
# 打开文件
# f = open("./hilichurl.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取文件-read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部字节的结果：{f.read()}")
# 读取文件-readlines()
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")
# 读取文件-readline()
# print(f"第一行数据的内容：{f.readline()}")
# print(f"第二行数据的内容：{f.readline()}")
# print(f"第三行数据的内容：{f.readline()}")
# for循环读取数据
# for line in f:
#     print(f"每一行数据：{line}")
# 文件的关闭
# f.close()
# with open语法
with open("./hilichurl.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据：{line}")
```

---

### 修纂文件
```python
# 文件的写入
f = open("./hilichurl.txt", "w", encoding="UTF-8")
# write写入
f.write("Olah！Olah！")
# flush刷新
f.flush()
# close关闭
f.close()
```

---

### 增添文件
```python
# 文件的追加写入
f = open("./hilichurl.txt", "a", encoding="UTF-8")
# write写入
f.write("\nYoyo mosi mita！")
# close关闭
f.close()
```
结束p7

---

## 异常非同小可
### 逮捕异常
```python
# 基本捕获语法
# try:
#     f = open("hilichurl.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常，改用w模式打开")
#     f = open("hilichurl.txt", "w", encoding="UTF-8")
# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现变量未定义异常")
    print(e)
# 捕获多个异常
try:
     1 / 0
     # print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现变量未定义或除零异常")
# 捕获所有异常
try:
    f= open("./hilichurl.txt", "r")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
finally:
    print("finally有没有异常都执行")
    f.close()
```

---

### 异常接力
```python
# 异常的传递
# 定义一个异常方法
def func1():
    print("func1开始")
    num = 1 / 0
    print("func1结束")


# 定义无异常方法调用上面方法
def func2():
    print("func2开始")
    func1()
    print("func2结束")


# 定义方法调用上面方法
def main():
    func2()

try:
    main()
except Exception as e:
    print(f"出现异常，信息是{e}")
```

---

### 装填模块
```python
# 模块导入
# import导入模块
# import time
# print("Olah！")
# time.sleep(3)
# print("Olah！")
# from导入模块
# from time import sleep
# print("Olah！")
# sleep(2)
# print("Olah！")
# 使用*导入全部功能
# from time import *
# print("Olah！")
# sleep(2)
# print("Olah！")
# 使用as添加别名
import time as t
print("Olah！")
t.sleep(2)
print("Olah！")
```

---

### 自封模块
```python
# 导入自定义模块
# from my_mod1 import test
#
# test(1, 4)
# 导入不同模块同名功能
from my_mod2 import test

test(1, 3)
# __main__变量
from my_mod1 import *

test(3, 4)
# __all__变量
testa(2, 3)
```

---

### 打包
```python
# 创建一个包
# 导入包中模块并使用
# import my_package.my_mod1
#
# my_package.my_mod1.modinfo()
# 通过__all__控制import*
from my_package import *

my_mod2.mod2()
```
结束p8

---

## 着手数据
### 准备json
```python
# 转为json
enemies = [{'name': 'slime', 'hp': 58}, {'name': 'hilichurl', 'hp': 73}]
json_enemies = json.dumps(enemies)
print(type(json_enemies))
print(json_enemies)
# json转为python数据
s = '[{"name": "slime", "hp": 58}, {"name": "hilichurl", "hp": 73}]'
l = json.loads(s)
print(type(l))
print(l)
```

---

### pyecharts门下
```python
# pyecharts入门
# 导入包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线对象
line = Line()
# 添加x轴数据
line.add_xaxis(['dull', 'silver', 'skyrider'])
# 添加y轴数据
line.add_yaxis("atk", [23, 33, 38])
# 全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="武器ATK", pos_left='center', pos_bottom='1%'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
# render方法生成图像
line.render()
```

---

### 打理数据
```python
# 处理数据
f_us = open("./美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jp = open("./日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("./印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()
# 去掉不合规范开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉不合规结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取y轴数据
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)
# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data)
line.add_yaxis("日本确诊人数", jp_y_data)
line.add_yaxis("印度确诊人数", in_y_data)
# 生成图表
line.render()
# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
```
结束p9

---

## 数据的演绎
### 全国地图环节
```python
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open('./疫情.txt', 'r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()
# 转换为字典
data_dict = json.loads(data)
# 取出省份的数据
province_data_list = data_dict['areaTree'][0]['children']
# 数据重组为元组列表
data_list = []
for province_data in province_data_list:
    if province_data['name'] == '新疆':
        province_name = '新疆维吾尔自治区'
    elif province_data['name'] == '西藏':
        province_name = '西藏自治区'
    elif province_data['name'] == '内蒙古':
        province_name = '内蒙古自治区'
    elif province_data['name'] == '宁夏':
        province_name = '宁夏回族自治区'
    elif province_data['name'] == '北京':
        province_name = '北京市'
    elif province_data['name'] == '天津':
        province_name = '天津市'
    elif province_data['name'] == '重庆':
        province_name = '重庆市'
    elif province_data['name'] == '广西':
        province_name = '广西壮族自治区'
    elif province_data['name'] == '上海':
        province_name = '上海市'
    else:
        province_name = province_data['name'] + '省'
    province_confirm = province_data['total']['confirm']
    data_list.append((province_name, province_confirm))
print(data_list)
# 创建地图对象
map = Map()
# 添加数据
map.add('各省确诊人数', data_list, 'china')
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title='全国疫情地图'),
    visualmap_opts=VisualMapOpts(
        is_show=True,       # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {'min': 1, 'max': 99, 'lable': '1~99人', 'color': '#CCFFFF'},
            {'min': 100, 'max': 999, 'lable': '100~999人', 'color': '#FFFF99'},
            {'min': 1000, 'max': 4999, 'lable': '1000~4999人', 'color': '#FF9966'},
            {'min': 5000, 'max': 9999, 'lable': '5000~9999人', 'color': '#FF6666'},
            {'min': 10000, 'max': 99999, 'lable': '10000~99999人', 'color': '#CC3333'},
            {'min': 100000, 'lable': '100000~人', 'color': '#990033'},

        ]
    )
)
# 绘图
map.render('全国疫情地图.html')
```

---

### 省级地图环节
```python
# 湖南省疫情图开发
# 读取文件
f = open('./疫情.txt', 'r', encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 获取数据
# json转字典
data_dict = json.loads(data)
# 取到湖南省数据
cities_data = data_dict['areaTree'][0]['children'][5]['children']
# 准备数据为元组
data_list = []
for city_data in cities_data:
    if city_data['name'] == '湘西自治州':
        city_name = '湘西土家族苗族自治州'
    else:
        city_name = city_data['name'] + '市'
    city_confirm = city_data['total']['confirm']
    data_list.append((city_name, city_confirm))
print(data_list)
# 构建地图
map = Map()
map.add('湖南省疫情地图', data_list, '湖南')
# 全局选项
map.set_global_opts(
    title_opts=TitleOpts(title='湖南疫情地图'),
    visualmap_opts=VisualMapOpts(
        is_show=True,       # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {'min': 1, 'max': 99, 'label': '1~99人', 'color': '#CCFFFF'},
            {'min': 100, 'max': 999, 'label': '100~999人', 'color': '#FFFF99'},
            {'min': 1000, 'max': 4999, 'label': '1000~4999人', 'color': '#FF9966'},
            {'min': 5000, 'max': 9999, 'label': '5000~9999人', 'color': '#FF6666'},
            {'min': 10000, 'max': 99999, 'label': '10000~99999人', 'color': '#CC3333'},
            {'min': 100000, 'label': '100000~人', 'color': '#990033'},

        ]
    )
)
# 绘图
map.render('湖南疫情地图.html')
```
结束p10

---

