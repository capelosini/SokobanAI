from datetime import datetime


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


class State:
    def __init__(self):
        self.data: list = []
        self.size = [-1, -1]
        self.varCount = 1  # For all added variables (ex: player pos)

    def successors(self):
        raise NotImplementedError

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

    def setupState(self, data):
        data = data.strip().replace(" ", "")

        self.size = [int((data.index("\n"))), data.count("\n") + 1]
        data = data.replace("\n", "")

        self.data = [c for c in data]

        startPos = self.data.index("🙎")

        self.data.append(startPos)  # start pos var

    def from_file(self, path):
        with open(path, "r+", encoding="utf-8") as f:
            data = f.read()

        self.setupState(data)

        return self

    def getId(self):
        data = [str(d) for d in self.data]
        return "".join(data)

    def export(self, toFile=False, title=""):
        out = ""
        i = 0
        while i < len(self.data) - self.varCount:
            out += str(self.data[i]) + " "
            i += 1
            if i % self.size[0] == 0:
                out += "\n"

        out = f"\n---- {datetime.now()} | {title}\n\n{out}"

        if toFile:
            with open("outputs.txt", "a+") as f:
                f.write(out)

        return out


class Visited:
    def __init__(self):
        self.set = set()

    def add(self, id: str):
        self.set.add(str(id))

    def wasVisited(self, id: str):
        return id in self.set

    def getAmount(self):
        return len(self.set)
