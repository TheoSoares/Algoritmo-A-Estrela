#include "node.h"

Node create_node(unsigned x, unsigned y) {
    Node n;
    n.exist = 1;
    n.x = x;
    n.y = y;
    return n;
}

unsigned array_length(Node *array) {
    for (unsigned i = 0;; i++) {
        if (array[i].exist != 1) {
            return i;
        }
    }
}

void reverse_array(Node *array) {
    unsigned array_size = array_length(array);
    Node temp;
    for (unsigned i = 0; i < array_size/2; i++) {
        temp = array[i];
        array[i] = array[array_size - i - 1];
        array[array_size - i - 1] = temp;
    }
}

void remove_from_array(Node *array, Node to_remove) {
    unsigned cont = 0;
    while (array[cont].exist == 1) {
        if ((array[cont].x == to_remove.x) && (array[cont].y == to_remove.y)) {
            break;
        }
        cont++;
    }
    while (array[cont + 1].exist == 1) {
        array[cont] = array[cont + 1];
        cont++;
    }
}

int search_in_array(Node *array, unsigned array_size, Node no) {
    for (unsigned i = 0; i < array_size; i++) {
        if ((array[i].x == no.x) && (array[i].y == no.y)) {
            return i;
        }
    }
    return -1;
}