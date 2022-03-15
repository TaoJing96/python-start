def list_append():
    a = [1, 2, 3]
    print(type(a))
    a.append(4)
    if 4 in a:
        print("4 in %s" % a)

    del a[0]
    for i in a.__add__([4, 5, 6]):
        print(i)


def list_add(arr):
    arr.append(2)


if __name__ == "__main__":
    list_append()
    arr = []
    print(arr)
    list_add(arr)
    print(arr)
