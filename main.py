from Game.Sokoban import Sokoban

game = Sokoban("input.txt")

next = game.initState.successors()

for i in next:
    state = i
    print(state.data)
    for j in state.successors():
        print(j.data)
