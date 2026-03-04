from Game.GreedyState import GreedyState
from Structures.Graph import Node

initState = GreedyState().from_file("input.txt")
root = Node(initState)

next = initState.successors()

for i in next:
    state = i
    print(state.data)
    for j in state.successors():
        print(j.data)
