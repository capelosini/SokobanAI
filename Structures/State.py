class State:
    def __init__(self):
        self.data = None
        self.size = [-1, -1]

    def successors(self):
        raise NotImplementedError

    def from_file(self, path):
        raise NotImplementedError
