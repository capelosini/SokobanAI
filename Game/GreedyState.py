from Structures.State import State


class GreedyState(State):
    def __init__(self, node):
        super().__init__(node)

    def from_file(self, path):
        with open(path, "r+", encoding="utf-8") as f:
            self.data = f.read().strip().replace(" ", "")

        self.size = [int((self.data.index("\n"))), self.data.count("\n") + 1]
        self.data = self.data.replace("\n", "")

        self.data = [c for c in self.data]

        startPos = self.data.index("🙎")

        self.data.append(startPos)  # start pos var

        return self

    def vector2ToIndex(self, x, y):
        return y * self.size[0] + x

    def canMove(self, index):
        if index < 0 or index >= (self.size[0] * self.size[1]):
            return False

        return self.data[index] != "🧱"

    def getPos(self):
        return self.data[-1]

    def setPos(self, pos):
        self.data[-1] = pos

    def successors(self):
        pos = self.getPos()
        positions = [pos + self.size[0], pos - self.size[0]]

        if (self.size[0] * self.size[1]) % (pos - (self.size[0] - 1)) != 0:
            positions.append(pos + 1)

        if pos != 0 and (self.size[0] * self.size[1]) % pos != 0:
            positions.append(pos - 1)

        if self.node.parent != None:
            lastPos = self.node.parent.value.getPos()
        else:
            lastPos = self.getPos()

        validPositions = list(
            filter(lambda p: self.canMove(p) and lastPos != p, positions)
        )

        for pos in validPositions:
            newNode = self.node.add_child(None)
            newState = GreedyState(newNode)
            newState.data = self.data[:]
            newState.size = self.size
            newState.setPos(pos)
            newNode.value = newState

        return self.node.children
