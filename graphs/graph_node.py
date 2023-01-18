class GraphNode:

    def __init__(self, value):
        self.__adjacent_nodes = []
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def add_node(self, node):
        if node not in self.__adjacent_nodes:
            self.__adjacent_nodes.append(node)

    @property
    def adjacent_nodes(self):
        return self.__adjacent_nodes

    def is_connected_to_node(self, node):
        return False