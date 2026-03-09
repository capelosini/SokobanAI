# Sokoban System Modeling / Modelagem do Sistema

> [!TIP]
> Click on the sections below to expand the content in your preferred language.
> Clique nas seções abaixo para expandir o conteúdo no seu idioma de preferência.

---

## 1. Problem Modeling / Modelagem do Problema

<details>
<summary><b>🇺🇸 English Version</b></summary>

### Successor Function
The successor function is responsible for generating the next possible states from the current state:
1. **Identification:** Maps all adjacent positions to the character.
2. **Validation:** Checks if the move violates rules (collision with walls or attempting to push two boxes simultaneously).
3. **Generation:** Creates new state objects, defining the movement direction.
4. **Storage:** Adds valid states to an array for processing by the search frontier.

### Goal Function
Game completion is governed by two main functions:
* `getFinalBoxesPositions`: Maps the coordinates of the target markings on the board where boxes should be delivered.
* `isEnd`: Verifies if the current box configuration exactly matches the target map.

### Cost Calculation
The path cost g(n) is calculated dynamically:
* **Free Movement:** Fixed cost of **1**.
* **Pushing a Box:** Cost of **1 + box weight**.

### Heuristic Function h(n)
We use the **Manhattan Distance** to estimate the cost to the goal. The formula applied between two points P_1(x_1, y_1) and P_2(x_2, y_2) is:
|x_1 - x_2| + |y_1 - y_2|

> **Why is the Heuristic admissible?**
> It is admissible because it provides an optimistic estimate. In a grid, it represents the shortest possible path between two points ignoring obstacles. Since the actual cost in Sokoban (with walls and detours) will always be equal to or greater than this distance, the function never overestimates the actual cost, ensuring optimality in the A* algorithm.
</details>

<details>
<summary><b>🇧🇷 Versão em Português</b></summary>

### Função Sucessora
A função sucessora é responsável por gerar os próximos estados possíveis a partir do estado atual:
1. **Identificação:** Mapeia todas as posições adjacentes ao personagem.
2. **Validação:** Verifica se o movimento viola as regras (colisão com paredes ou tentativa de empurrar duas caixas simultâneas).
3. **Geração:** Cria os novos objetos de estado, definindo a direção do movimento.
4. **Armazenamento:** Adiciona os estados válidos em um array para processamento pela fronteira de busca.

### Função Objetivo
A conclusão do jogo é regida por duas funções principais:
* `getFinalBoxesPositions`: Mapeia as coordenadas das marcações no tabuleiro onde as caixas devem ser entregues.
* `isEnd`: Verifica se a configuração atual das caixas coincide exatamente com o mapa de objetivos.

### Cálculo de Custo
O custo do caminho $g(n)$ é calculado de forma dinâmica:
* **Movimento Livre:** Custo fixo de **1**.
* **Empurrar Caixa:** Custo de **1 + peso da caixa**.

### Função Heurística $h(n)$
Utilizamos a **Distância de Manhattan** para estimar o custo até o objetivo. A fórmula aplicada entre dois pontos P_1(x_1, y_1) e P_2(x_2, y_2) é:
|x_1 - x_2| + |y_1 - y_2|

> **Por que a Heurística é admissível?**
> Ela é admissível porque fornece uma estimativa otimista. Em um grid, ela representa o menor caminho possível entre dois pontos ignorando obstáculos. Como o custo real no Sokoban (com paredes e desvios) sempre será igual ou maior que essa distância, a função nunca superestima o custo real, garantindo a otimalidade no algoritmo A*.
</details>

---

## 2. State Management / Gerenciamento de Estados



<details>
<summary><b>🇺🇸 English Version</b></summary>

To optimize resource usage, states are handled as follows:
* **Compression:** The 2D board mapping is converted into a single `string` for fast comparison.
* **Data Structures:** States are kept in memory using:
    * `Visited`: A Set to avoid reprocessing already explored states.
    * `Stack` / `Queue`: Collections to manage expansion order (LIFO/FIFO).
</details>

<details>
<summary><b>🇧🇷 Versão em Português</b></summary>

Para otimizar o uso de recursos, os estados são tratados da seguinte forma:
* **Compactação:** O mapeamento do tabuleiro 2D é convertido em uma `string` única para facilitar a comparação rápida.
* **Estruturas de Dados:** Os estados são mantidos em memória utilizando:
    * `Visited`: Conjunto (Set) para evitar o reprocessamento de estados já explorados.
    * `Stack` / `Queue`: Coleções para gerenciar a ordem de expansão (LIFO/FIFO).
</details>

---

## 3. Case Study: Complexity / Estudo de Caso: Complexidade



Sokoban is known for its **PSPACE-complete** complexity. The growth of possible combinations is exponential as the grid area and number of elements increase.

| Grid Size | Total Area (Cells) | Relative Complexity |
| :--- | :--- | :--- |
| 8 x 8 | 64 | Low / Baixa |
| 16 x 16 | 256 | Medium / Média |
| 24 x 24 | 576 | High / Alta |
| 64 x 64 | 4,096 | Critical / Crítica |
