flag = False
arr = []

def say(num: int, num2: int):
    print("%d" % (num + num2))


class Person(object):
    name = 0

    def __init__(self, name):
        self.name = name

    def fcn(self, val=400):
        val3 = 300
        self.val4 = val
        self.val5 = 500

    def __list_emement__(self):
        for name, value in vars(self).items():
            print("%s,%s" % (name, value))


if __name__ == "__main__":
    p = Person(2)
    print(type(p.name))
    p.__list_emement__()
    p = Person("221中午")
    print(type(p.name))
    p.__list_emement__()
