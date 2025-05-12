# Comparação de Implementações do Algoritmo A* em Diferentes Linguagens

Este repositório contém implementações do algoritmo A* em quatro linguagens de programação distintas, com o objetivo de comparar a **facilidade de leitura e escrita** entre elas. O trabalho faz parte de um projeto acadêmico, no qual analisamos como diferentes linguagens afetam a clareza e a concisão do código, especialmente em algoritmos clássicos como o A*.

## Linguagens Utilizadas

- **Python** (linguagem extra, não analisada)
- **Java**
- **C**
- **Ruby**

Cada uma dessas linguagens oferece diferentes paradigmas, estilos de sintaxe e níveis de abstração. Nosso objetivo é observar como essas diferenças impactam o entendimento e desenvolvimento do algoritmo.

## O que é o Algoritmo A*?

O A* (A-estrela) é um algoritmo de busca heurística utilizado para encontrar o **caminho mais curto** entre dois pontos em um grafo, como em mapas ou tabuleiros de jogos. Ele combina os conceitos de busca em largura (BFS) e busca de custo uniforme (UCS), usando uma função heurística para guiar a exploração de caminhos promissores.

### Funcionamento

O A* usa uma função de custo `f(n)` para cada nó `n`, definida como:

**f(n) = g(n) + h(n)**

- `g(n)` é o custo do caminho desde o nó inicial até o nó `n`.
- `h(n)` é uma heurística que estima o custo do nó `n` até o destino.

A heurística deve ser **admissível**, ou seja, nunca superestimar o custo real até o destino, para garantir que o A* encontre o caminho mais curto.

### Exemplo de Aplicação

- Navegação em mapas (GPS)
- Inteligência artificial em jogos (ex: movimentação de NPCs)
- Resolução de quebra-cabeças (como o quebra-cabeça de 8 peças)

## Objetivo da Comparação

Durante o desenvolvimento, observamos os seguintes aspectos:

- Quantidade de código necessário
- Clareza e legibilidade da sintaxe
- Facilidade de implementar estruturas de dados auxiliares (como filas de prioridade)

Esses fatores serão discutidos em nosso relatório final, com exemplos retirados diretamente das implementações presentes neste repositório.

## Contribuição

Este projeto foi desenvolvido por estudantes como parte de um trabalho da disciplina de Linguagens de Programação.

Integrantes do projeto: [Théo Corvello Soares](https://github.com/TheoSoares), [Luis Henrique Kiekhofel Reichow](https://github.com/HenriqueReichow), [Othávio Christmann Correa](https://github.com/othaviocc) e [Matheus Nunes Buttow](https://github.com/matheusbuttow)

