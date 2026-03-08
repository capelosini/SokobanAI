import sys

from Game.Dijkstra import dijkstra
from Game.Sokoban import Sokoban

inputPath = "input.txt"
if len(sys.argv) > 1:
    inputPath = sys.argv[1]

game = Sokoban(inputPath)
# (qtd_estados_visitados, no_solucao) = dijkstra(game)


game.bfs()
