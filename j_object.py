"""
第十一章：对象
"""

# 01 类的定义
from typing import Union

"""
class 类名称
    类的属性
    类的方法

方法的定义
def fuc(self,参数1,...)
调用时不用管self

self:指代对象本身

构造方法(初始化对象)
def __init__(self,...):
    ...
    
魔术方法：
def __str__(self)       将对象转变为字符串
def __lt__(self,other)  小于符号比较，other是另一个对象，该方法定义对象大小关系，返回true或false
def __le__(self,other)  小于等于比较
def __eq__(self,other)  等于比较

私有成员和方法
以__开头命名

单继承
class child(father):
    ...
    
多继承
class child(father1,father2,...)

pass关键字：占位语句

调用父类方法：利用父类名 或 super

类型注解(让IDE可以推断数据类型，便于提示)
基础语法：变量:类型  val:int = 3,容器还可以详细注解 my_tuple:
也可以通过注释
对形参进行类型注解一样是用基础语法
返回值在函数定义冒号前加 ->返回类型

Union类型
联合类型：union[类型1，类型2]

抽象类：每个方法都用pass代替内容，从而让子类具体实现功能
"""


class stu:
    name = None

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"hello,{self.name}")


stu1 = stu("lee")
# stu1.name = "lee"
stu1.say_hi()

my_tuple1: tuple[int, str, bool] = (1, "ok", True)
my_tuple2 = (1, "ok", True)  # type: tuple[int, str, bool]


def add(a: int, b: int) -> int:
    return a + b


a: Union[int, str] = None
