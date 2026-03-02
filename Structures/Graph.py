class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, value):
        newNode = Node(value)
        newNode.parent = self

        self.children.append(newNode)
        return newNode

    def remove_child(self, node):
        self.children.remove(node)

    def __str__(self):
        return f"{self.value}\n{'-' * len(str(self.value))}\n{'   '.join([str(n.value) for n in self.children])}"
