import json
from pyecharts.charts import Map
from pyecharts.options import *
# # 读取数据文件
# f = open('./疫情.txt', 'r', encoding='UTF-8')
# data = f.read()
# # 关闭文件
# f.close()
# # 转换为字典
# data_dict = json.loads(data)
# # 取出省份的数据
# province_data_list = data_dict['areaTree'][0]['children']
# # 数据重组为元组列表
# data_list = []
# for province_data in province_data_list:
#     if province_data['name'] == '新疆':
#         province_name = '新疆维吾尔自治区'
#     elif province_data['name'] == '西藏':
#         province_name = '西藏自治区'
#     elif province_data['name'] == '内蒙古':
#         province_name = '内蒙古自治区'
#     elif province_data['name'] == '宁夏':
#         province_name = '宁夏回族自治区'
#     elif province_data['name'] == '北京':
#         province_name = '北京市'
#     elif province_data['name'] == '天津':
#         province_name = '天津市'
#     elif province_data['name'] == '重庆':
#         province_name = '重庆市'
#     elif province_data['name'] == '广西':
#         province_name = '广西壮族自治区'
#     elif province_data['name'] == '上海':
#         province_name = '上海市'
#     elif province_data['name'] == '香港':
#         province_name = '香港特别行政区'
#     elif province_data['name'] == '澳门':
#         province_name = '澳门特别行政区'
#     else:
#         province_name = province_data['name'] + '省'
#     province_confirm = province_data['total']['confirm']
#     data_list.append((province_name, province_confirm))
# print(data_list)
# # 创建地图对象
# map = Map()
# # 添加数据
# map.add('各省确诊人数', data_list, 'china')
# # 设置全局选项
# map.set_global_opts(
#     title_opts=TitleOpts(title='全国疫情地图'),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,       # 是否显示
#         is_piecewise=True,  # 是否分段
#         pieces=[
#             {'min': 1, 'max': 99, 'label': '1~99人', 'color': '#CCFFFF'},
#             {'min': 100, 'max': 999, 'label': '100~999人', 'color': '#FFFF99'},
#             {'min': 1000, 'max': 4999, 'label': '1000~4999人', 'color': '#FF9966'},
#             {'min': 5000, 'max': 9999, 'label': '5000~9999人', 'color': '#FF6666'},
#             {'min': 10000, 'max': 99999, 'label': '10000~99999人', 'color': '#CC3333'},
#             {'min': 100000, 'label': '100000~人', 'color': '#990033'},
#
#         ]
#     )
# )
# # 绘图
# map.render('全国疫情地图.html')

# ===========================================================================================

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