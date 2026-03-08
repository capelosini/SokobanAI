from Game.Sokoban import Sokoban
from Game.Dijkstra import dijkstra

game = Sokoban("input.txt")
#(qtd_estados_visitados, no_solucao) = dijkstra(game)


game.bfs()
