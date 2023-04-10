# 基本捕获语法
# try:
#     f = open("hilichurl.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常，改用w模式打开")
#     f = open("hilichurl.txt", "w", encoding="UTF-8")
# 捕获指定异常
# import my_mod1
import my_package.my_mod1

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
    f = open("./hilichurl.txt", "r")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
finally:
    print("finally有没有异常都执行")
    f.close()


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
# import time as t
#
# print("Olah！")
# t.sleep(2)
# print("Olah！")

# 导入自定义模块
# from my_mod1 import test
#
# test(1, 4)
# 导入不同模块同名功能
# from my_mod2 import test

# test(1, 3)
# __main__变量
# from my_mod1 import *

# test(3, 4)
# __all__变量
# testa(2, 3)

# 创建一个包
# 导入包中模块并使用
# import my_package.my_mod1
#
# my_package.my_mod1.modinfo()
# 通过__all__控制import*
from my_package import *

my_mod2.mod2()
