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
# with open("./hilichurl.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据：{line}")

# 文件的写入
# f = open("./hilichurl.txt", "w", encoding="UTF-8")
# # write写入
# f.write("Olah！Olah！")
# # flush刷新
# f.flush()
# # close关闭
# f.close()

# 文件的追加写入
f = open("./hilichurl.txt", "a", encoding="UTF-8")
# write写入
f.write("\nYoyo mosi mita！")
# close关闭
f.close()
