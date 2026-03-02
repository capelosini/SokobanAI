class State:
    def __init__(self, node):
        self.data = None
        self.size = [-1, -1]
        self.node = node

    def successors(self):
        raise NotImplementedError

    def from_file(self, path):
        raise NotImplementedError
