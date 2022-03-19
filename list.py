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


def multi_list():
    arr = [[0] * 3] * 4 # 3行4列 这样每个子列表指向相同地址
    arr[0][0] = 1
    print(arr) # [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
    arr = [[0 for i in range(3)] for i in range(4)] # 正确生成二维数组
    arr[0][0] = 1
    print(arr)


if __name__ == "__main__":
    list_append()
    arr = []
    print(arr)
    list_add(arr)
    print(arr)
    multi_list()

