class Node:

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def append(self, node):
        if type(node) is not Node:
            raise Exception("Not a node")
        else:
            self.__next = node

    @property
    def next(self):
        return self.__next

    @property
    def value(self):
        return self.__value

    @property
    def size(self):
        if self.__next is None:
            return 1
        else:
            return 1 + self.__next.size



