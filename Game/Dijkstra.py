from Game.GameStates import SokobanState
from Game.Structures import Node, PriorityQueue, Visited


def resultado(resultado):
    no_resultado = "🙎 - - - - 🟢🧱🧱1 8 - - 🧱 - - - - 🧱 - - - 🟢 - - -"
    if no_resultado == resultado:
        return True
    else:
        return False


def dijkstra():
    no = Node()

    fila = PriorityQueue()
    fila.push(no, no.cost)
    visitados = Visited()

    while not fila.esta_vazio():
        (prioridade, no) = fila.pop()
        visitados.add(no)

        if resultado(no.value):
            return (visitados.getAmount(), no)

        nos_sucessores = SokobanState.successors(no)

        for no_sucessor in nos_sucessores:
            if not visitados.wasVisited(no_sucessor):
                # fazer função de custo
                custo_da_aresta = 1
                # custo acumulado
                novo_custo_total = no.custo + custo_da_aresta

                if novo_custo_total < no_sucessor.custo:
                    no_sucessor.custo = novo_custo_total
                    no_sucessor.parent = no
                    fila.push(no_sucessor, novo_custo_total)

    return (visitados.getAmount(), None)
