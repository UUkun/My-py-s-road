# 基础柱状图
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# # bar构建基础柱状图
# bar = Bar()
# # 添加x轴数据
# bar.add_xaxis(['dull', 'silver', 'skyrider'])
# # 添加y轴数据
# bar.add_yaxis("atk", [23, 33, 38], label_opts=LabelOpts(position='right'))
# # 反转xy轴
# bar.reversal_axis()
# # 绘图
# bar.render('基础bar图.html')

# 有时间线的bar图
# bar1 = Bar()
# bar1.add_xaxis(['dull', 'silver', 'skyrider'])
# bar1.add_yaxis("atk", [23, 33, 38], label_opts=LabelOpts(position='right'))
# bar1.reversal_axis()
# bar2 = Bar()
# bar2.add_xaxis(['dull', 'silver', 'skyrider'])
# bar2.add_yaxis("atk", [68, 91, 105], label_opts=LabelOpts(position='right'))
# bar2.reversal_axis()
# bar3 = Bar()
# bar3.add_xaxis(['dull', 'silver', 'skyrider'])
# bar3.add_yaxis("atk", [113, 151, 171], label_opts=LabelOpts(position='right'))
# bar3.reversal_axis()
# # 构建时间线对象
# timeline = Timeline({'theme': ThemeType.WALDEN})
# # 时间线内添加bar
# timeline.add(bar1, 'Level1/20')
# timeline.add(bar2, 'Level20/40')
# timeline.add(bar3, 'Level40/50')
# # 自动播放设置
# timeline.add_schema(
#     play_interval=1000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=True
# )
# # 用时间线绘图
# timeline.render('基础时间线bar图.html')

# GDP动态图
f = open('1960-2019全球GDP数据.csv', 'r', encoding='GB2312')
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除首行
data_lines.pop(0)
# 数据转换为字典
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    # 判断字典里有无key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 创建时间线对象
timeline = Timeline({'theme': ThemeType.DARK})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出前八
    year_data = data_dict[year][:8]
    x_data = list()
    y_data = list()
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP（亿）', y_data, label_opts=LabelOpts(position='right'))
    # 反转xy轴
    bar.reversal_axis()
    # 每年图表标题
    bar.set_global_opts(title_opts=TitleOpts(title=f'{year}年全球前八GDP'))
    timeline.add(bar, f'{year}')

# 自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 绘图
timeline.render('gdp前八国家.html')
