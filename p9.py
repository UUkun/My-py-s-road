import json

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

# pyecharts入门
# 导入包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线对象
# line = Line()
# # 添加x轴数据
# line.add_xaxis(['dull', 'silver', 'skyrider'])
# # 添加y轴数据
# line.add_yaxis("atk", [23, 33, 38])
# # 全局配置
# line.set_global_opts(
#     title_opts=TitleOpts(title="武器ATK", pos_left='center', pos_bottom='1%'),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
# render方法生成图像
# line.render()

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
