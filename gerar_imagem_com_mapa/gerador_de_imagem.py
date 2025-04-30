from PIL import Image
import numpy as np

def gerar_imagem(caminho_arquivo):
    # Abre o arquivo e lê a matriz
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
    
    # Prepara uma lista de listas com os valores da matriz
    matriz = []
    for linha in linhas:
        matriz.append([char for char in linha.strip()])
    
    # Converte a matriz para um array numpy
    altura = len(matriz)
    largura = len(matriz[0])
    
    # Cria uma imagem com o tamanho da matriz
    imagem = Image.new('RGB', (largura, altura))
    pixels = imagem.load()
    
    # Mapeamento de cores para os valores
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
    
    # Preenche a imagem com os valores da matriz
    for y in range(altura):
        for x in range(largura):
            valor = matriz[y][x]
            if valor in cores:
                pixels[x, y] = cores[valor]
    
    # Salva a imagem gerada como PNG
    imagem.save('matriz_imagem.png')
    print("Imagem gerada com sucesso: matriz_imagem.png")

# Caminho do arquivo com a matriz (substitua pelo caminho correto)
caminho_arquivo = input()
gerar_imagem(caminho_arquivo)
