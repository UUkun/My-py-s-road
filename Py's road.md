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