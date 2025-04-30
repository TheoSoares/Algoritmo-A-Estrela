#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "node.h"

void save_txt(char **matrix, char *map_path, unsigned rows) {
    FILE *archive;
    char *solved_map_path = malloc(sizeof(char) * (strlen(map_path) + 7));
    solved_map_path = strcpy(solved_map_path, map_path);
    solved_map_path[strlen(solved_map_path) - 4] = 0;
    solved_map_path = strcat(solved_map_path, "_solved.txt");
    archive = fopen(solved_map_path, "w");

    for (unsigned i = 0; i < rows; i++) {
        fprintf(archive, "%s", matrix[i]);
        if (i + 1 < rows) {
            fprintf(archive, "\n");
        }
    }

    fclose(archive);

    free(solved_map_path);
}

char direction(Node atual, Node next) {
    Node dir;
    dir.x = atual.x - next.x;
    dir.y = atual.y - next.y;

    if (dir.x == 1) {
        return '^';
    }
    else if (dir.x == -1) {
        return 'v';
    }
    else if (dir.y == 1) {
        return '<';
    }
    else {
        return '>';
    }
}

void write_map(char *map_path, Node *solve_path, unsigned **matrix, unsigned *size, Node *start, Node *goal) {
    char **new_matrix;
    new_matrix = malloc(sizeof(char*) * size[0]);
    for (unsigned i = 0; i < size[1]; i++) {
        new_matrix[i] = malloc(sizeof(char) * (size[1] + 1));
    }

    for (unsigned i = 0; i < size[0]; i++) {
        for (unsigned j = 0; j < size[1]; j++) {
            new_matrix[i][j] = matrix[i][j] + '0';
        }
    }

    free(matrix);

    for (unsigned i = 1; ((solve_path[i].x != goal->x) || (solve_path[i].y != goal->y)); i++) {
        new_matrix[solve_path[i].x][solve_path[i].y] = direction(solve_path[i], solve_path[i + 1]);
    }

    save_txt(new_matrix, map_path, size[0]);
}