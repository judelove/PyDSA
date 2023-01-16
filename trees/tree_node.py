class TreeNode:

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.right()

    '''Assign a node as a left child of this node'''
    @left.setter
    def left(self, value):
        self.__left = TreeNode(value)

    '''Assign a node as a right child of this node'''
    @right.setter
    def right(self, value):
        self.__right = TreeNode(value)

    def contains(self, value):
        if self.__value == value:
            return True
        else:
            return (self.__left is not None and self.__left.contains(value)) or (self.__right is not None and self.__right.contains(value))

    @property
    def height(self):
        left_height = 0
        right_height = 0
        if self.__left is not None:
            left_height = self.__left.height
        if self.__right is not None:
            right_height = self.__right.height

        return 1 + max(left_height, right_height)