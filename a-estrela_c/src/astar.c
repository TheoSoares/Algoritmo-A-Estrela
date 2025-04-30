#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "node.h"
#include "writemap.h"

void matrix_size(char *filename, unsigned *size) {
    char buffer[1024];
    size[0] = 0;

    FILE *archive = fopen(filename, "r");
    
    while (fgets(buffer, sizeof(buffer), archive) != NULL) {
        buffer[strcspn(buffer, "\n")] = 0;
        size[0]++;
    }
    size[1] = strlen(buffer);

    fclose(archive);
}

void map_to_matrix(char *filename, unsigned **matrix, Node *start, Node *goal) {
    char buffer[1024];
    unsigned row = 0;

    FILE *archive = fopen(filename, "r");

    while (fgets(buffer, 1024, archive) != NULL) {
        buffer[strcspn(buffer, "\n")] = 0;
        for (unsigned i = 0; i < strlen(buffer); i++) {
            matrix[row][i] = buffer[i] - '0';
            if (matrix[row][i] == 2) {
                start[0] = create_node(row, i);
            }
            if (matrix[row][i] == 3) {
                goal[0] = create_node(row, i);
            }
        }
        row++;
    }

    fclose(archive);
}

void fill_matrix_with_infinity(double **matrix, unsigned *size) {
    for (unsigned i = 0; i < size[0]; i++) {
        for (unsigned j = 0; j < size[1]; j++) {
            matrix[i][j] = INFINITY;
        }
    }
}

unsigned get_vizinhos(Node *array, Node atual, unsigned **matrix, unsigned *size) {
    Node novo;
    unsigned cont = 0;
    double dir[] = {1, 0, -1, 0, 0, 1, 0, -1};
    for (int i = 0; i < 4; i++) {
        novo = create_node(atual.x + dir[(i * 2)], atual.y + dir[(i * 2) + 1]);
        if ((0 <= novo.x) && (novo.x < size[1]) && (0 <= novo.y) && (novo.y < size[0])) {
            if (matrix[novo.x][novo.y] != 1) {
                array[cont] = novo;
                cont++;
            }
        }
    }
    return cont;
}

unsigned heuristic(Node  *no, Node  *goal) {
    return (abs(no->x - goal->x) + abs(no->y - goal->y));
}

Node *astar(Node *start, Node *goal, unsigned **matrix, unsigned *size) {
    unsigned open_size;
    Node *open, **came_from;
    double **g_score, **f_score;
    open = malloc(sizeof(Node) * size[0] * size[1]);

    came_from = malloc(sizeof(Node*) * size[0]);
    for (unsigned i = 0; i < size[0]; i++) {
        came_from[i] = malloc(sizeof(Node) * size[1]);
    }

    g_score = malloc(sizeof(double*) * size[0]);
    for (unsigned i = 0; i < size[0]; i++) {
        g_score[i] = malloc(sizeof(double) * size[1]);
    }
    
    f_score = malloc(sizeof(double*) * size[0]);
    for (unsigned i = 0; i < size[0]; i++) {
        f_score[i] = malloc(sizeof(double) * size[1]);
    }

    fill_matrix_with_infinity(f_score, size);
    fill_matrix_with_infinity(g_score, size);

    open[0] = create_node(start->x, start->y);
    open_size = 1;
    g_score[start->x][start->y] = 0;
    f_score[start->x][start->y] = heuristic(start, goal);

    while (open_size > 0) {
        Node best = open[0];
        for (unsigned i = 0; i < open_size; i++) {
            if (f_score[open[i].x][open[i].y] < f_score[best.x][best.y]) {
                best = open[i];
            }
        }
        
        if ((best.x == goal->x) && (best.y == goal->y)) {
            Node *path;
            path = malloc(sizeof(Node) * size[0] * size[1]);
            for (unsigned i = 0; best.exist == 1; i++) {
                path[i] = best;
                best = came_from[best.x][best.y];
            }
            reverse_array(path);
            free(open);
            free(came_from);
            return path;
        }
        
        remove_from_array(open, best);
        open_size--;
        
        Node *vizinhos;
        double custo;
        vizinhos = malloc(sizeof(Node) * 4);
        unsigned vizinhos_size = get_vizinhos(vizinhos, best, matrix, size);
        for (unsigned i = 0; i < vizinhos_size; i++) {
            custo = g_score[best.x][best.y] + 1;
            if (custo < g_score[vizinhos[i].x][vizinhos[i].y]) {
                came_from[vizinhos[i].x][vizinhos[i].y] = best;
                g_score[vizinhos[i].x][vizinhos[i].y] = custo;
                f_score[vizinhos[i].x][vizinhos[i].y] = custo + heuristic(&vizinhos[i], goal);
                if (search_in_array(open, open_size, vizinhos[i]) == -1) {
                    open[open_size] = vizinhos[i];
                    open_size++;
                }
            }
        }
        free(vizinhos);
    }

    free(open);
    free(came_from);
    Node *ptr;
    ptr = malloc(sizeof(Node));
    ptr[0] = create_node(0, 0);
    ptr[0].exist = 0;
    return ptr;
}

int main() {
    char *map_path = malloc(sizeof(char) * 200);
    printf("Insira o caminho absoluto do mapa: ");
    map_path = fgets(map_path, 200, stdin);
    map_path[strcspn(map_path, "\n")] = 0;
    map_path = realloc(map_path, strlen(map_path));

    Node *start, *goal;
    start = malloc(sizeof(Node));
    goal = malloc(sizeof(Node));

    unsigned *size = malloc(sizeof(unsigned) * 2);
    matrix_size(map_path, size);

    unsigned **matrix;
    matrix = malloc(sizeof(unsigned*) * size[0]);
    for (unsigned i = 0; i < size[0]; i++) {
        matrix[i] = malloc(sizeof(unsigned) * size[1]);
    }

    map_to_matrix(map_path, matrix, start, goal);

    Node *path;
    path = malloc(sizeof(Node) * (size[0] * size[1]));

    path = astar(start, goal, matrix, size);

    if (path[0].exist != 1) {
        printf("Não há um caminho possível!");
        return 0;
    }

    write_map(map_path, path, matrix, size, start, goal);
}