def tuple_add():
    a = (1, 2, 3)
    for i in range(len(a)):
        print(i)
    print("%x" % id(a))
    b = a + (4, )
    print("%x" % id(b))


if __name__ == "__main__":
    tuple_add()
