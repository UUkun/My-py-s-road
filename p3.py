# while循环
exp = 0
i = 0
while i < 100:
    i += 1
    exp += i
    print(f"第{i}次练级，经验为{exp}")

# while嵌套
i = 0
while i < 7:
    j = 0
    i += 1
    while j < 10:
        j += 1
        print(f"第{i}天的第{j}只丘丘人")

# for循环
name = "Lata movo dada"
i = 0
for x in name:
    if x == 'a':
        i += 1
print(f"\"Lata movo dada\"里有{i}个\'a\'")

# range语句
for x in range(4):
    print(f"{x}个丘丘病了")

# for循环嵌套
for i in range(1, 8):
    for j in range(1, 11):
        print(f"第{i}天的第{j}只丘丘人")

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
