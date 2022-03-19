class Creature:
    def say(self):
        print("Creature say")

    def work(self):
        print("Creature work")


class Person(Creature):
    kind = "person"

    def __init__(self, name):
        self.sex = 'woman'
        self._weight = '190'
        self.__age = 0
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name or 'no name'

    @name.deleter
    def name(self):
        print("name.deleter")

    def say(self):
        super().work()
        print("Person say")

    @staticmethod
    def staticMethod():
        print("staticMethod")

    @classmethod
    def classMethod(cls):
        cls.kind = 'human' # 类方法 必须传类对象
        print("classMethod")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("非法类型")
    age = property(get_age, set_age) #也可以设置property


# mro 多继承时使用mro来解决方法冲突的问题
class Chinese(Person, Creature):
    def work(self):
        print("Chinese work")


if __name__ == "__main__":
    p = Person('tt')
    p.work()  # 继承
    p.say()
    print(p.name)
    p.name = '33'
    print(p.name) # 修改name
    Person.staticMethod()
    Person.classMethod()
    del p.name # 调用@name.deleter
    print(p.name)
    print(p.age)
    p.age = 10
    print(p.age)
    p.age = "10"
    print(p.__dict__)
    print(p._Person__age) # 名字重整 私有变量加前置实现私有性
    print(Person.__dict__)
    p.kind = "p" # 改变不了类变量
    p.__class__.kind = "pp" # 可以改变类变量
    print(Person.kind)
