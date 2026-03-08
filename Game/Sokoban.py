from Game.GameStates import SokobanState
from Game.Structures import Node, Queue, Stack, Visited
from Game.Utils import isNumber


class Sokoban:
    def __init__(self, fileInput: str):
        self.initState = SokobanState().fromFile(fileInput)
        self.root = Node(self.initState)
        self.finalBoxesPositions = self.initState.getFinalBoxesPositions()

    def isEnd(self, state):
        for i in self.finalBoxesPositions:
            if not isNumber(state.data[i]):
                return False
        return True

    def dfs(self):
        visited = Visited()
        visited.add(self.root.value.getId())

        stack = Stack()
        stack.push(self.root)
        while stack.size() != 0:
            node = stack.pop()
            state = node.value
            print(state.export())
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    stack.push(newNode)

    def bfs(self):
        visited = Visited()
        visited.add(self.root.value.getId())

        queue = Queue()
        queue.add(self.root)

        while queue.size() != 0:
            node = queue.remove()
            state = node.value
            print(state.export())
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    queue.add(newNode)
