from Game.GreedyState import GreedyState
from Structures.Graph import Node

root = Node()
initState = GreedyState(root).from_file("input.txt")
root.value = initState

next = initState.successors()

for i in next:
    state = i.value
    print(state.data)
    for j in state.successors():
        print(j.value.data)
