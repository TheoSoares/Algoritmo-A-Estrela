def ler_mapa(caminho)
  File.readlines(caminho).map { |linha| linha.strip.chars.map(&:to_i) }
end

def vizinhos(posicao, mapa)
  x, y = posicao
  movimentos = [[1,0], [-1,0], [0,1], [0,-1]]
  movimentos.map { |dx, dy| [x + dx, y + dy] }
           .select do |nx, ny|
             nx.between?(0, mapa.size - 1) &&
             ny.between?(0, mapa[0].size - 1) &&
             [0, 3].include?(mapa[nx][ny])
           end
end

def heur(a, b)
  (a[0] - b[0]).abs + (a[1] - b[1]).abs
end

def reconstruir_caminho(ant, atual)
  caminho = [atual]
  while ant[atual]
    atual = ant[atual]
    caminho.unshift(atual)
  end
  caminho
end

def a_estrela(mapa, ini, fim)
  aberta = [[heur(ini, fim), ini]]
  fechada = []
  g = { ini => 0 }
  f = { ini => heur(ini, fim) }
  ant = {}

  until aberta.empty?
    aberta.sort_by!(&:first)
    _, atual = aberta.shift
    return reconstruir_caminho(ant, atual) if atual == fim

    fechada << atual
    vizinhos(atual, mapa).each do |v|
      next if fechada.include?(v)
      g_v = g[atual] + 1
      if !g[v] || g_v < g[v]
        ant[v] = atual
        g[v] = g_v
        f[v] = g_v + heur(v, fim)
        aberta << [f[v], v]
      end
    end
  end
  nil
end

def encontrar_inicio_fim(mapa)
  ini = fim = nil
  mapa.each_with_index do |linha, i|
    linha.each_with_index do |v, j|
      ini = [i, j] if v == 2
      fim = [i, j] if v == 3
    end
  end
  [ini, fim]
end

mapa = ler_mapa("mapaN.txt")
ini, fim = encontrar_inicio_fim(mapa)
caminho = a_estrela(mapa, ini, fim)

if caminho
  puts "Caminho Encontrado:"
  puts caminho.inspect
else
  puts "Nenhum caminho encontrado"
end
