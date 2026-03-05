from Game.GameStates import GreedyState
from Structures import Node


class Sokoban:
    def __init__(self, fileInput: str):
        self.initState = GreedyState().from_file(fileInput)
        self.root = Node(self.initState)
