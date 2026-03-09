import sys

from Game.Dijkstra import dijkstra
from Game.Sokoban import Sokoban

inputPath = "input.txt"
if len(sys.argv) > 1:
    inputPath = sys.argv[1]

game = Sokoban(inputPath)
# (qtd_estados_visitados, no_solucao) = dijkstra(game)


bfsResult = game.bfs()
game.printPathStepByStep(bfsResult)
game.printPath(bfsResult, title="BFS", exportFile="output/BFS.txt")
game.printPath(game.dfs(), title="DFS", exportFile="output/DFS.txt")
game.printPath(game.dijkstra(), title="Dijkstra", exportFile="output/Dijkstra.txt")
game.printPath(game.greedy(), title="Greedy", exportFile="output/Greedy.txt")
game.printPath(game.aStar(), title="A*", exportFile="output/AStar.txt")
