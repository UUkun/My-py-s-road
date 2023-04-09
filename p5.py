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

# 列表遍历
# while循环
index = 0
while index < len(enemies):
    print(enemies[index])
    index += 1
# for循环
for enemy in enemies:
    print(enemy)

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

# 数据容器切片
# 对list切片
print(f"enemies切片：{enemies[1:3]}")
# 对list切片 步长-1
print(f"enemies切片步长-1：{enemies[::-1]}")

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
