def writemap(mapa, map_path, solve_path):
    if solve_path == None:
        exit("Um caminho não foi encontrado!")
    map_path = map_path[:-4] + "_solved.txt"
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(len(solve_path))[1:-1]:
        for j, dir in enumerate(directions):
            if (solve_path[i + 1][0] == solve_path[i][0] + dir[0]) and (solve_path[i + 1][1] == solve_path[i][1] + dir[1]):
                match j:
                    case 0:
                        char = 'v'
                    case 1:
                        char = '^'
                    case 2:
                        char = '>'
                    case 3:
                        char = '<'
        mapa[solve_path[i][0]][solve_path[i][1]] = char
        
    with open(map_path, 'w') as archive:
        for index, i in enumerate(mapa):
            for j in i:
                archive.write(str(j))
            if index + 1 < len(mapa):
                archive.write("\n")