from Game.Structures import State


class GreedyState(State):
    def __init__(self):
        super().__init__()

    def successors(self):
        pos = self.getPos()
        positions = [pos + self.size[0], pos - self.size[0]]

        if ((pos + 1) % self.size[0]) != 0:
            positions.append(pos + 1)

        if ((pos) % self.size[0]) != 0:
            positions.append(pos - 1)

        validPositions = list(filter(lambda p: self.canMove(p), positions))

        states = []

        for pos in validPositions:
            newState = GreedyState()
            newState.data = self.data[:]
            newState.size = self.size
            newState.setPos(pos)
            states.append(newState)

        return states
