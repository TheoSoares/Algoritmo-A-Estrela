import writemap as wm

def ler_mapa(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
    mapa = []
    for linha in linhas:
        mapa.append([int(x) for x in linha.strip()])

    return mapa

def get_start_and_goal(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 2:
                start = (i,j)
            if mapa[i][j] == 3:
                goal = (i,j)

    return start,goal

def h(n, goal): #heuristica
    return abs(n[0] - goal[0]) + abs(n[1] - goal[1])

def getVizinhos(n, mapa):
    vizinhos = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)] #baixo, cima, direita, esquerda
    for dir in directions:
        novo = (n[0] + dir[0], n[1] + dir[1])
        if 0 <= novo[0] < len(mapa) and 0 <= novo[1] < len(mapa[0]):
            if mapa[novo[0]][novo[1]] !=1:
                vizinhos.append(novo)

    return vizinhos

def aStar(start, goal, mapa):
    aberto = [start]  #começa só com o início
    cameFrom = {}  #caminho
    gScore = {start: 0}  #custo pra chegar aqui
    fScore = {start: h(start, goal)}  #custo + heurística

    while len(aberto) > 0:
        melhor = aberto[0]
        for nodo in aberto:
            if fScore.get(nodo, float('inf')) < fScore.get(melhor, float('inf')):
                melhor = nodo

        if melhor == goal:
            caminho = [melhor]
            while melhor in cameFrom:
                melhor = cameFrom[melhor]
                caminho.append(melhor)
            caminho.reverse()
            return caminho
        aberto.remove(melhor)

        for vizinho in getVizinhos(melhor, mapa):
            custo = gScore[melhor] + 1
            if custo < gScore.get(vizinho, float('inf')):
                cameFrom[vizinho] = melhor
                gScore[vizinho] = custo
                fScore[vizinho] = custo + h(vizinho, goal)
                if vizinho not in aberto:
                    aberto.append(vizinho)

    return None

map_path = input("Insira o caminho absoluto do mapa: ")
mapa = ler_mapa(map_path)
start,goal = get_start_and_goal(mapa)
solve_path = aStar(start=start, goal=goal, mapa=mapa)

wm.writemap(mapa=mapa, map_path=map_path, solve_path=solve_path)