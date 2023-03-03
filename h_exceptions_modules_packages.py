"""
第九章：异常，模块，和包
"""

# 01 异常
"""
异常：程序运行过程中出现的错误

异常的捕获（异常的处理）：
对bug进行提醒和处理
语法：
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码

捕获目标错误，例如：
# try:
#     可能发生错误的代码
# except NameError as e: //这里e是错误的对象
#     如果出现异常执行的代码

捕获多个异常：
# try:
#     可能发生错误的代码
# except (NameError, ZeroDivisionError) as e:
#     如果出现异常执行的代码

捕获所有异常
# try:
#     可能发生错误的代码
# except Exception as e:
#     如果出现异常执行的代码

可加else和finally：
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
# else:
#     没有异常的动作
# finally:
# 都要执行的动作

异常的传递：
异常可从内层函数传递到外层函数
当所有函数都没有捕获异常时，程序会报错
"""

# 02 模块
"""
模块：module，是一个python文件，模块能定义函数，类，变量
其实就是工具包

导入模块：[from 模块名] import [模块|类|变量|函数|*][as 别名]
例如：
import 模块名
from 模块名 import ...

同名的，后导入的会覆盖前面的

自定义模块：
导入模块时，会运行模块内容
__main__变量

#if __name__ == '__main__':
当run这个文件时，__name__变量会被置为__main__

__all__变量
__all__ = [],[]中代表了*可用的变量和函数
"""

# 03 python包
"""
自定义包
一个文件夹，其下包含了一个__init__.py文件，该文件可用于包含多个模块文件
也有__all__变量

安装第三方包
numpy，pandas，...
安装命令：pip install 包名
国内镜像网站安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
"""
