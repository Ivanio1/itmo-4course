//
// Created by egor on 08.09.24.
//

#ifndef DISTRIBUTED_LAB1_MODEL_H
#define DISTRIBUTED_LAB1_MODEL_H
#include <sys/types.h>

struct PipeData {
    int8_t child_count; //without parent
    int process_id;
    int8_t last_read;
    int (*pipes)[11][2];
};

#endif //DISTRIBUTED_LAB1_MODEL_H
