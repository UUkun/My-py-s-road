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

### 初识变量
```python
# 万恶之源
primogem = 5600
# 花费十连*1
primogem = primogem - 1600
print('花费一个十连，还剩', primogem, '原石')
```
*与变量的相逢总是平淡却不平凡*

### 相遇的第一件事
```python
print(type("name"))
print(type(primogem))
print(type(2800.00))
```
*君の名は。*

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
```