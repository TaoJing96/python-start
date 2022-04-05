class NodeIter:
    def __init__(self, node):
        self.node = node

    # 迭代对象
    def __next__(self):
        if self.node is None:
            raise StopIteration
        node, self.node = self.node, self.node.next
        return node


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    # 返回迭代器
    def __iter__(self):
        return NodeIter(self)


# yield生成器
def fibonacci(n):
    a, b, num = 1, 1, 1
    while True:
        if num > n:
            return
        yield a
        a, b, num = b, a + b, num + 1


def generator_demo():
    for i in fibonacci(5):
        print(i)


if __name__ == '__main__':
    n1 = Node("n1")
    n2 = Node("n2")
    n1.next = n2
    print(dir(n1))
    for n in n1:
        print(n.name)
    print("generator_demo")
    generator_demo()
