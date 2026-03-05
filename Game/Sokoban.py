from Game.GameStates import GreedyState
from Game.Structures import Node, Queue, Stack, Visited


class Sokoban:
    def __init__(self, fileInput: str):
        self.initState = GreedyState().fromFile(fileInput)
        self.root = Node(self.initState)

    def dfs(self):
        visited = Visited()
        visited.add(self.root.value.getId())

        stack = Stack()
        stack.push(self.root)
        while stack.size() != 0:
            node = stack.pop()
            state = node.value
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    stack.push(newNode)
                    print(nextState.export())

    def bfs(self):
        visited = Visited()
        visited.add(self.root.value.getId())

        queue = Queue()
        queue.add(self.root)

        while queue.size() != 0:
            node = queue.remove()
            state = node.value
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    queue.add(newNode)
                    print(nextState.export())
