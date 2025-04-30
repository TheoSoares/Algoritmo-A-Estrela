#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

typedef struct {
    int exist;
    unsigned x;
    unsigned y;
} Node;

Node create_node(unsigned x, unsigned y);

unsigned array_length(Node *array);

void reverse_array(Node *array);

void remove_from_array(Node *array, Node to_remove);

int search_in_array(Node *array, unsigned array_size, Node no);

#endif