from typing import Optional, Union

import a
import math


def if_basic():
    i = 0 if 1 > 2 and 2 < 3 else 1
    print(i)


def while_basic():
    i = 5
    while i > 0:
        print(i)
        i -= 1


def for_basic():
    i = (2, 3, 4)
    j = (3, 4, 5) #元组不能add
    i = i + j
    # print(type(i))
    for n in i:
        if n > 2:
            break
        print(n)


def range_basic():
    for i in range(1, 2): # 2不会输出
        print(i)
    for i in range(2, 1, -1): # -1是步长 1不会输出
        print(i)

def pass_basic():
    if 1 > 2:
        print("impossible")
    else:
        # pass就是空语句，什么作用都没有
        pass
        print("possible")


# 打印所有属性和方法
def dir_basic():
    print(dir(a))
    print(dir())


def optional_basic(i: Optional[int] = None):
    print(i)


def union_basic(i: Union[int, None] = None):
    print(i)


def mod_basic():
    print(5 % 1e+9)
    print(5 % 10 ** 9) # 取模后为整数


def args_basic():
   args(1, 'a', 'b', name="tj", gender="sex")


def args(age, *args, **kwargs):
    print("args")
    print(age)
    print(args)
    print(kwargs)
    args_copy(age, *args, kwargs) # kwargsa 放入args元组中了
    args_copy(age, *args, **kwargs)


def args_copy(age, *args, **kwargs):
    print("args_copy")
    print(age)
    print(args)
    print(kwargs)


if __name__ == "__main__":
    print("if_basic")
    if_basic()
    print("while_basic")
    while_basic()
    print("for_basic")
    for_basic()
    print("pass_basic")
    pass_basic()
    print("dir_basic")
    dir_basic()
    print("range_basic")
    range_basic()
    print("optional_basic")
    optional_basic()
    optional_basic(1)
    print("union_basic")
    union_basic()
    union_basic(1)
    print("mod_basic")
    mod_basic()
    print("args_basic")
    args_basic()