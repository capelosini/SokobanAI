from Game.Structures import Directions, State
from Game.Symbols import *
from Game.Utils import isNumber, numbersTable, swap


class SokobanState(State):
    def __init__(self):
        super().__init__()
        self.direction = None
        self.cost = 0

    def getFinalBoxesPositions(self):
        positions = []
        for i in range(len(self.data)):
            if self.data[i] == TARGET:
                positions.append(i)
        return positions

    def up(self, index):
        if index < 0:
            return index
        return index - self.size[0]

    def down(self, index):
        if index < 0:
            return index
        return index + self.size[0]

    def left(self, index):
        if index < 0:
            return index

        if index % self.size[0] == 0:
            return -1

        return index - 1

    def right(self, index):
        if index < 0:
            return index

        newPos = index + 1
        if newPos % self.size[0] == 0:
            return -1
        return newPos

    def getDirection(self, fromIndex, index):
        move = index - fromIndex
        if move == 1:
            return Directions.Right
        elif move == -1:
            return Directions.Left
        elif move == self.size[0]:
            return Directions.Down
        elif move == -self.size[0]:
            return Directions.Up
        else:
            return Directions.Unknown

    def canMove(self, fromIndex, index):
        if (
            index < 0
            or index >= (self.size[0] * self.size[1])
            or self.data[index] == WALL
        ):
            return False

        object = self.data[index]

        if isNumber(object):
            direction = self.getDirection(fromIndex, index)
            if (
                (
                    direction == Directions.Right
                    and not self.canMove(index, self.right(index))
                )  # Right
                or (
                    direction == Directions.Left
                    and not self.canMove(index, self.left(index))
                )  # Left
                or (
                    direction == Directions.Down
                    and not self.canMove(index, self.down(index))
                )  # Down
                or (
                    direction == Directions.Up
                    and not self.canMove(index, self.up(index))
                )  # Up
            ):
                return False

        return True

    def successors(self):
        pos = self.getPos()
        positions = [self.up(pos), self.down(pos), self.left(pos), self.right(pos)]

        validPositions = list(filter(lambda p: self.canMove(pos, p), positions))

        states = []

        for newPos in validPositions:
            newState = SokobanState()
            newState.data = self.data[:]
            newState.size = self.size
            newState.setPos(newPos)

            direction = self.getDirection(pos, newPos)
            newState.direction = direction

            if isNumber(self.data[newPos]):
                indexA = newPos
                indexB = newPos

                if direction == Directions.Right:
                    indexB = self.right(newPos)
                elif direction == Directions.Left:
                    indexB = self.left(newPos)
                elif direction == Directions.Down:
                    indexB = self.down(newPos)
                elif direction == Directions.Up:
                    indexB = self.up(newPos)
                swap(newState.data, indexA, indexB)
                newState.cost = numbersTable[self.data[newPos]]

            newState.cost += 1

            states.append(newState)

        return states
