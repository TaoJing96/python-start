class Creature:
    def say(self):
        print("Creature say")

    def work(self):
        print("Creature work")


class Person(Creature):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name or 'no name'

    def say(self):
        super().work()
        print("Person say")

    @staticmethod
    def staticMethod():
        print("staticMethod")

    @classmethod
    def classMethod(cls):
        print("classMethod")


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
