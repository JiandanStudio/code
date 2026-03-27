# -*- coding: utf-8 -*-
# @Author  : Jian
# @FileName:
# @Time    : 2022/3/19 18:22
import pandas
from pyecharts.charts import Sankey
from pyecharts import options as opts

data = pandas.read_excel("file:///Users/wangshenghua/Desktop/sankey_data.xlsx", sheet_name='Sheet1')

nodes = []
for i in set(pandas.concat([data.FROM, data.TO])):
    d1 = {}
    d1["name"] = i
    print(d1)
    nodes.append(d1)
print(nodes)

# nodes = []
#
# for i in range(2):
#     values = data.iloc[:, i].unique()
#     for value in values:
#         dic = {}
#         dic['name'] = value
#         nodes.append(dic)
# print(nodes)


links = []
for x, y, z in zip(data.FROM, data.TO, data.VALUE):
    d2 = {}
    d2['source'] = x
    d2['target'] = y
    d2['value'] = z
    links.append(d2)
pic = (
    Sankey(init_opts=opts.InitOpts(width="1600px", height="800px")).add("销售数据",  # 图例名称
                                                                        nodes,  # 传入节点数据
                                                                        links,  # 传入边和流量数据
                                                                        # 设置透明度、弯曲度、颜色
                                                                        linestyle_opt=opts.LineStyleOpts(opacity=0.5,
                                                                                                         curve=0.5,
                                                                                                         color="source"),
                                                                        # 标签显示位置 right/top
                                                                        label_opts=opts.LabelOpts(position="right"),
                                                                        node_gap=10,  # 节点之前的距离
                                                                        # orient="vertical"  # 垂直显示
                                                                        ).set_global_opts(
        title_opts=opts.TitleOpts(title="数据统计"))
)
pic.render("数据统计.html")


