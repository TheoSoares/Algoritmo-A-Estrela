import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

def get_start_and_goal(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 2:
                start = (i, j)
            elif mapa[i][j] == 3:
                goal = (i, j)
    return start, goal

def h(n, goal):
    return abs(n[0] - goal[0]) + abs(n[1] - goal[1])

def getVizinhos(n, mapa):
    vizinhos = []
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = n[0]+dx, n[1]+dy
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and mapa[nx][ny] != 1:
            vizinhos.append((nx, ny))
    return vizinhos

def update_image(mapa, visitados, vizinhos_atuais, caminho_final, iteracao, pasta="gif_frames", apagar_azul=False, last_loop=0):
    imagem = np.ones((len(mapa), len(mapa[0]), 3))

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 1:
                imagem[i][j] = [0, 0, (last_loop % 2) / 255]
            elif mapa[i][j] == 2:
                imagem[i][j] = [1, 0, 0]
            elif mapa[i][j] == 3:
                imagem[i][j] = [0, 1, 0]

    if not apagar_azul:
        for i, j in visitados:
            imagem[i][j] = [0.2, 0.2, 1.0]

    for i, j in vizinhos_atuais:
        imagem[i][j] = [1.0, 0.5, 0.0]

    for i, j in caminho_final:
        imagem[i][j] = [1.0, 0, 0]

    plt.imshow(imagem)
    plt.axis('off')
    os.makedirs(pasta, exist_ok=True)
    plt.savefig(os.path.join(pasta, f"iter_{iteracao:03d}.png"), bbox_inches='tight', pad_inches=0)
    plt.close()

def aStar(start, goal, mapa, pasta="gif_frames"):
    aberto = [start]
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: h(start, goal)}
    visitados = set()
    iteracao = 0

    while aberto:
        atual = min(aberto, key=lambda x: fScore.get(x, float('inf')))
        if atual == goal:
            caminho = [atual]
            while atual in cameFrom:
                atual = cameFrom[atual]
                caminho.append(atual)
            caminho.reverse()

            update_image(mapa, visitados, [], caminho, iteracao, apagar_azul=True)
            for i in range(9):  # pausa final
                update_image(mapa, visitados, [], caminho, iteracao+i+1, apagar_azul=True, last_loop=(i + 1))
            return caminho

        aberto.remove(atual)
        vizinhos = getVizinhos(atual, mapa)
        for vizinho in vizinhos:
            if vizinho not in visitados:
                visitados.add(vizinho)
            novo_g = gScore[atual] + 1
            if novo_g < gScore.get(vizinho, float('inf')):
                cameFrom[vizinho] = atual
                gScore[vizinho] = novo_g
                fScore[vizinho] = novo_g + h(vizinho, goal)
                if vizinho not in aberto:
                    aberto.append(vizinho)

        update_image(mapa, visitados, vizinhos, [], iteracao)
        iteracao += 1
    return None

def ler_mapa(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
    mapa = []
    for linha in linhas:
        mapa.append([int(x) for x in linha.strip('\n')])

    return mapa

def gerar_gif(path="gif_frames"):
    files = sorted(os.listdir(path))
    print(files)
    frames = [Image.open(os.path.join(path, fig)) for fig in files]
    frames[0].save("a_estrela.gif", save_all=True, append_images=frames, duration=20, loop=0) # duration -> tempo em ms de cada frame (50 fps -> duration=20)

mapa = ler_mapa(input("Insira o caminho absoluto do mapa: "))
start, goal = get_start_and_goal(mapa)
print("Início:", start, "Fim:", goal)

caminho = aStar(start, goal, mapa)
gerar_gif()