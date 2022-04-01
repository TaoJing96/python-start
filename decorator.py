# 函数装饰器
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func(*args, **kwargs)
        print("call done")
        return res


@Timer
def add(a, b):
    return a + b


# 类装饰器
def my_str(cls):
    def __str__(self):
        return 'new str'
    cls.__str__ = __str__
    return cls


# 类装饰器 等价于my_str(MyObject)
@my_str
class MyObject:
    pass


if __name__ == "__main__":
    # 等价于print(Timer(add(2, 3)))
    print(add(2, 3))
    print(MyObject())