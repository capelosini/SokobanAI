from datetime import datetime

from Game.Symbols import *
from Game.Utils import Directions, isNumber


class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.children = []
        self.cost = 0

    def addChild(self, value):
        newNode = Node(value)
        newNode.parent = self
        newNode.cost = self.cost + value.cost

        self.children.append(newNode)
        return newNode

    def removeChild(self, node):
        self.children.remove(node)

    def __str__(self):
        return f"{self.value}\n{'-' * len(str(self.value))}\n{'   '.join([str(n.value) for n in self.children])}"


class State:
    def __init__(self):
        self.data: list = []
        self.size = [-1, -1]
        self.varCount = 1  # For all added variables (ex: player pos)

    def successors(self):
        raise NotImplementedError

    def vector2ToIndex(self, x, y):
        return y * self.size[0] + x

    def getPos(self):
        return self.data[-1]

    def setPos(self, pos):
        self.data[-1] = pos

    def setupState(self, data):
        data = data.strip().replace(" ", "")

        self.size = [int((data.index("\n"))), data.count("\n") + 1]
        data = data.replace("\n", "")

        self.data = [c for c in data]

        startPos = self.data.index(PLAYER)

        self.data.append(startPos)  # start pos var

    def fromFile(self, path):
        with open(path, "r+", encoding="utf-8") as f:
            data = f.read()

        self.setupState(data)

        return self

    def getId(self):
        data = [str(d) for d in self.data]
        return "".join(data)

    def export(self, toFile=False, title="", finalBoxesPosition=[]):
        data = self.data[:]
        out = ""
        i = 0
        playerPos = self.getPos()
        while i < len(data) - self.varCount:
            if data[i] == PLAYER:
                data[i] = EMPTY
            if i in finalBoxesPosition and not isNumber(data[i]):
                data[i] = TARGET
            if i == playerPos:
                data[i] = PLAYER

            out += str(data[i]) + " "
            i += 1
            if i % self.size[0] == 0:
                out += "\n"

        if title:
            out = f"\n---- {datetime.now()} | {title}\n\n{out}"
        else:
            out = f"\n\n{out}"

        if toFile:
            with open("outputs.txt", "a+") as f:
                f.write(out)

        return out


class Visited:
    def __init__(self):
        self.set = set()

    def add(self, id: str):
        self.set.add(str(id))

    def wasVisited(self, id: str):
        return id in self.set

    def getAmount(self):
        return len(self.set)


class Stack:
    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()


class Queue:
    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def add(self, value):
        self.array.append(value)

    def remove(self):
        return self.array.pop(0)


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, prioridade):
        # Inserimos uma tupla (prioridade, item)
        elemento = (prioridade, item)
        self.heap.append(elemento)
        # Agora precisamos "consertar" o heap subindo o elemento (Bubble Up)
        self._subir(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("A fila está vazia")

        # 1. Pega o menor item (que está sempre na raiz/índice 0)
        menor_item = self.heap[0]

        # 2. Move o último elemento da lista para a raiz
        ultimo_item = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo_item
            # 3. "Conserta" o heap descendo o elemento (Sink Down / Heapify)
            self._descer(0)

        # Retorna apenas o menor item
        # (a tupla é (prioridade, item))
        return menor_item

    def _subir(self, indice):
        # Enquanto não for a raiz
        while indice > 0:
            pai_indice = (indice - 1) // 2

            # Se o filho for MENOR que o pai, troca (Min-Heap)
            if self.heap[indice][0] < self.heap[pai_indice][0]:
                self._trocar(indice, pai_indice)
                indice = pai_indice
            else:
                break

    def _descer(self, indice):
        tamanho = len(self.heap)

        while True:
            menor = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            # Verifica se o filho da esquerda existe e é menor que o atual
            if esquerda < tamanho and self.heap[esquerda][0] < self.heap[menor][0]:
                menor = esquerda

            # Verifica se o filho da direita existe e é menor que o menor encontrado até agora
            if direita < tamanho and self.heap[direita][0] < self.heap[menor][0]:
                menor = direita

            # Se o menor não for o índice atual, precisamos trocar e continuar descendo
            if menor != indice:
                self._trocar(indice, menor)
                indice = menor
            else:
                # O elemento já está na posição certa (é menor que seus filhos)
                break

    def _trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def esta_vazio(self):
        return len(self.heap) == 0
