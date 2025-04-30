from PIL import Image
import numpy as np

def gerar_imagem(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
    
    matriz = []
    for linha in linhas:
        matriz.append([char for char in linha.strip()])
    
    altura = len(matriz)
    largura = len(matriz[0])
    
    imagem = Image.new('RGB', (largura, altura))
    pixels = imagem.load()
    
    cores = {
        '0': (255, 255, 255),  # Branco
        '1': (0, 0, 0),        # Preto
        '2': (255, 0, 0),      # Vermelho
        '3': (0, 255, 0),      # Verde
        '<': (0, 0, 255),      # Azul (para caminho)
        '>': (0, 0, 255),      # Azul (para caminho)
        'v': (0, 0, 255),      # Azul (para caminho)
        '^': (0, 0, 255)       # Azul (para caminho)
    }
    
    for y in range(altura):
        for x in range(largura):
            valor = matriz[y][x]
            if valor in cores:
                pixels[x, y] = cores[valor]
    
    imagem.save(caminho_arquivo[:-4] + '_imagem.png')
    print("Imagem gerada com sucesso: matriz_imagem.png")

caminho_arquivo = input()
gerar_imagem(caminho_arquivo)
