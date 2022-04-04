class NodeIter:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        if self.node is None:
            raise StopIteration
        node, self.node = self.node, self.node.next
        return node


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)


if __name__ == '__main__':
    n1 = Node("n1")
    n2 = Node("n2")
    n1.next = n2
    print(dir(n1))
    for n in n1:
        print(n.name)
