"""
第十章：数据可视化
"""

# Echarts，pyecharts

# 01 折线图
"""
json数据格式
json轻量级的数据交互格式，本质上是一个带有特定格式的字符串
负责在不同编程语言间进行数据的传递和交互
"""
import json

# 准备符合json格式要求的python数据
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]
# 通过json.dumps()把python数据转化为了json数据
data = json.dumps(data, ensure_ascii=False) #ensure_ascii是是否将字符转为ascii码
print(data)
print(type(data))
# 通过json.loads()把json数据转化为了python数据
data = json.loads(data)
print(data)
print(type(data))


