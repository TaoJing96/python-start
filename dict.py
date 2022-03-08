def dict_add():
    a = dict()
    a[2] = 2
    a[2] = 3 # 更新
    a["s"] = 2
    for k, v in a.items():
        print("k:%s, v:%s" % (k, v))
    # for k in a:
    #     print("k:%s, v:%s" % (k, a[k]))


def dict_delete():
    a = dict()
    a[2] = 2
    s = a.pop(2)
    print(s)
    print(type(s))
    s = a.pop(4, 'not found')
    print(s)


if __name__ == "__main__":
    dict_add()
    print("dict_delete")
    dict_delete()