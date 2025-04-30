#ifndef WRITEMAP_H_INCLUDED
#define WRITEMAP_H_INCLUDED
#include "node.h"

void write_map(char *map_path, Node *solve_path, unsigned **matrix, unsigned *size, Node *start, Node *goal);

#endif