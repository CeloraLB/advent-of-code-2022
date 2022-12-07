class Node:
    def __init__(self, name: str, size: int, parent = None):
        self.size = size
        self.name = name
        self.parent = parent

class DirNode (Node):
    def __init__(self, name: str, parent: Node = None):
        super().__init__(name, 0, parent)
        self.childrens = {}

    def __str__(self) -> str:
        children_str = []
        for node in self.childrens:
            children_str.append(node.__str__())
        return '{}: {}'.format(self.name, '\n'.join(children_str))

    def addChildren(self, node: Node):
        self.childrens[node.name] = node
        self.updateSize(node.size)

    def updateSize(self, size: int):
        self.size += size
        if not self.parent is None:
            self.parent.updateSize(size)

class FileNode (Node):
    def __init__(self, name: str, parent: Node = None, size: int = 0):
        super().__init__(name, size, parent)

    def __str__(self) -> str:
        return '{}: {}'.format(self.name, self.size)
