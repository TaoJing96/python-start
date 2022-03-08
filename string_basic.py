

def string_basic():
    a = "abc"
    b = '''a
        b'''
    print(b)
    print(a * 2)
    if "a" in a:
        print("a in %s" % a)


def string_join():
    k = 'a'.join(('1', '2', '3'))
    print(type(k))
    print(k)


if __name__ == "__main__":
    string_basic()
    print("string_join")
    string_join()