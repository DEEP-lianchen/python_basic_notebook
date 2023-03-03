"""
第七章：函数进阶
"""

# 01 函数的多返回值
"""
可以 return1，2 来返回两个值
"""

# 02 函数的多种传参方式
"""
指明参数名与值对应，不必按顺序（关键字传参）
或者，按形参顺序传参 （位置传参）
定义函数时，可以设置默认值，这时候调用函数时可缺省参数

不定长参数：
1）位置传递
def user_info(*args)
args 会被默认为元组
2）关键字传递
def user_info(**kwargs)
传参时，按照“键=值”的形式进行传参
传入kwargs中，组成字典

"""

# 03 匿名函数
"""
1）函数作为参数传递
相当于传入一种计算的逻辑，供已有数据进行使用
相当于函数是多态的
2）lambda 匿名函数
无名称的匿名函数只能临时用一次,只能写一行
e.g. lambda x,y:x+y
"""