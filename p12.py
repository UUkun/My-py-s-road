# 设计类
class Enemy:

    def __init__(self, name: str, level: int, hp: int, atk: int, __def: int):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.__def = __def

    def __str__(self):
        return f'名字：{self.name}，等级：{self.level}，生命：{self.hp}，攻击：{self.atk}'

    # 封装
    def __attacked(self, atk: int):
        self.hp -= atk

    def attacked(self, atk: int):
        self.__attacked(int(atk * (500 / (500 + self.__def))))
    # 创建对象


enemy_1 = Enemy('hilichurl', 1, 73, 46, 505)
# 输出对象信息
print(enemy_1)
enemy_1.attacked(40)
print(enemy_1)


# 继承
class EliteEnemy(Enemy):

    def __init__(self, name, level, hp, atk, __def, ele: str):
        super().__init__(name, level, hp, atk, __def)
        self.element = ele

    def __str__(self):
        return super().__str__() + f', 元素：{self.element}'


e_enemy1 = EliteEnemy('Hydro Abyss Mage', 1, 146, 76, 505, 'hydro')
print(e_enemy1)


def trap(enemy: Enemy):
    enemy.attacked(90)


trap(e_enemy1)
print(e_enemy1)


