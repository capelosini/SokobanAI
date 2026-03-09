import time

from Game.GameStates import SokobanState
from Game.Structures import Node, PriorityQueue, Queue, Stack, Visited
from Game.Symbols import *
from Game.Utils import isNumber


class Sokoban:
    def __init__(self, fileInput: str):
        self.initState = SokobanState().fromFile(fileInput)
        self.finalBoxesPositions = self.initState.getFinalBoxesPositions()
        self.lastVisited = None

    def isEnd(self, state):
        for i in self.finalBoxesPositions:
            if not isNumber(state.data[i]):
                return False
        return True

    def printPathStepByStep(self, resultNode):
        if resultNode == None:
            return
        self.printPathStepByStep(resultNode.parent)
        state = resultNode.value
        exported = state.export(finalBoxesPosition=self.finalBoxesPositions)
        time.sleep(0.7)
        print(exported)
        if state.direction:
            print(DIRECTIONS[state.direction])

    def printPath(self, resultNode):
        node = resultNode
        directions = ""
        i = 0
        while node != None:
            state = node.value
            if state.direction:
                directions = DIRECTIONS[state.direction] + " " + directions
                i += 1

            if node.parent == None:
                exported = resultNode.value.export(
                    finalBoxesPosition=self.finalBoxesPositions
                )
                print(exported)
                print(f"Movements:\n{directions}")
                print(f"Movements Count:\n{i}")
                if self.lastVisited != None:
                    print(f"Total states:\n{self.lastVisited.getAmount()}")

            node = node.parent

    def dfs(self):
        visited = Visited()
        root = Node(self.initState)
        visited.add(root.value.getId())

        stack = Stack()
        stack.push(root)
        while stack.size() != 0:
            node = stack.pop()
            state = node.value
            # print(state.export())
            if self.isEnd(state):
                self.lastVisited = visited
                return node
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    stack.push(newNode)

    def bfs(self):
        visited = Visited()
        root = Node(self.initState)
        visited.add(root.value.getId())

        queue = Queue()
        queue.add(root)

        while queue.size() != 0:
            node = queue.remove()
            state = node.value
            # print(state.export())
            if self.isEnd(state):
                self.lastVisited = visited
                return node
            for nextState in state.successors():
                id = nextState.getId()
                if not visited.wasVisited(id):
                    visited.add(id)
                    newNode = node.addChild(nextState)
                    queue.add(newNode)

    def dijkstra(self):
        root = Node(self.initState)

        fila = PriorityQueue()
        fila.push(root, root.cost)
        visitados = Visited()

        while not fila.esta_vazio():
            priority, currentNode = fila.pop()
            state = currentNode.value
            visitados.add(state.getId())

            if self.isEnd(state):
                self.lastVisited = visitados
                return currentNode

            newStates = state.successors()

            for newState in newStates:
                if not visitados.wasVisited(newState.getId()):
                    visitados.add(newState.getId())
                    newNode = currentNode.addChild(newState)
                    if currentNode.cost < newNode.cost:
                        fila.push(newNode, newNode.cost)

        return (visitados.getAmount(), None)
