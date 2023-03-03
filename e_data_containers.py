"""
第六章：数据容器
"""

# 01 数据容器
"""
一种可以存储多个元素的python数据类型
分为五种：
列表list，元组tuple，字符串str，集合set，字典dict
"""

# 02 列表 list
"""
[元素1，元素2,...]
或者 变量名 = list()
列表中元素类型可不同，列表可嵌套

下标索引：0，1，2，...n-1
也可以反向寻找：-1,-2,....

列表常用操作，方法：
1）查询元素：查找指定元素第一个匹配的的下标，找不到，则报错ValueError
myList.index(查询元素)
2）插入元素：
myList.insert(指定下标，指定插入元素)
3）修改元素：直接修改即可
4）追加元素：直接加到尾部
myList.append(加入元素)
5）追加一批元素
myList.extend(另一列表)
6）删除元素
方式1：del myList[指定下标]
方式2：myList.pop(指定下标)，同时可以返回这个值
7）删除某元素的第一匹配项
myList.remove(目标元素)
8）列表清空：
myList.clear()
9）统计指定元素数量
myList.count()
10)列表长度
len(myList)

list的遍历：
while相比for：可以自定义循环条件
"""
myList = ["123", "abc", "yer", "abc"]
print(type(myList))
index = myList.index("abc")
print(index)
print(len(myList))

# 03 元组 tuple
"""
元组同列表一样，都是可以封装多个不同类型的元素
但元组一旦定义完成，便不可修改，即只读的list

定义：myTuple = (元素1，元素2，...)
myTuple = tuple()

元组的操作：
myTuple.index()
myTuple.count()
len(myTuple)

若元组中嵌套了一个list，list中元素可修改
"""

# 04 字符串 str
"""
也支持下标
字符串时不可修改的数据容器

myStr.index()
1）字符串的替换：将字符串内的全部字符串1替换为字符串2，实际字符串未修改，而是形成了新的字符串
myStr.replace(字符串1，字符串2, [几个])
2）字符串的分割：按照指定分割符，将其分割成多个字符串，并存入列表对象中
myStr.split(分割字符)
3）字符串规整操作：
去掉前后空格：myStr.strip()
去掉前后指定字符串：myStr.strip(指定字符串)，其实是去除这个字符串的每个字符
4）myStr.count(),len(myStr)
"""

myStr = " 你说如果我，我是说如果我，想牵你的手说你"
newStr = myStr.replace("我", "我们", 2)
print(myStr)
print(newStr)
newList = myStr.split("，")
print(newList)
newStr = myStr.strip("你说手 ")
print(newStr)

# 05 数据容器(序列)的切片
"""
序列：内容连续，有序，可使用下标索引的一类数据容器
即列表，元组，字符串
切片：取序列的一个子序列
语法：序列[起始下标(默认从头)：结束下标(不含本身，默认结尾)：步长(默认为1，可为负，反向取，但要注意起始和结尾下标也要反向)]
"""

# 06 集合 set
"""
{元素1，元素2,...}
mySet=set()
不支持下标索引

集合操作：
添加元素：mySet.add()
删除元素：mySet.remove()
随机取出一个元素：mySet.pop()
清空集合：mySet。clear()
取两个集合的差集：mySet3 = mySet1.difference(mySet2)
消除差集：mySet1.difference_update(mySet2)
取两集合并：mySet1.union(mySet2)
"""

# 07 字典 dict
"""
Key:Value
myDict = {Key1:Value1,Key2:Value2,Key2:Value2,...}
myDict = dict()

字典中key不可重复，只保留后面的（后面的会覆盖）
只能通过Key进行索引
字典可嵌套

字典常用操作：
1）新增和更新都是：myDict[Key] = Value
2）删除元素：my_dict.pop(Key)
3）清空元素：myDict.keys()，得到全部key

字典不能进行while循环
"""

myDict = {1: 'a', 2: 'b', 3: 'c'}
keys = myDict.keys()
print(keys)
print(type(keys))

# 08 其他通用操作
"""
max()
min()
类型转换

序列排序：sorted(序列，[reverse = true](是否反转)),返回列表
"""