#include <stdio.h>
#include <unistd.h>
#include "ipc.h"
#include "model.h"
#include "common.h"
//1 - read/write success
//0 - no data
//-1 - error

int send(void *self, local_id dst, const Message *msg) {
    struct PipeData *pipeData = (struct PipeData *) self;
    int *pipe = pipeData->pipes[pipeData->process_id][dst];
    ssize_t wrote = 0;
    while (wrote < sizeof(*msg)) {
        ssize_t wrote_tmp = write(pipe[1], msg, sizeof(Message));
        if (wrote_tmp == -1) {
            return -1;
        }
        if (wrote_tmp == 0) {
            return 0;
        }
        wrote += wrote_tmp;
    }
    return 1;
}

int send_multicast(void *self, const Message *msg) {
    struct PipeData *pipeData = (struct PipeData *) self;
    for (int8_t i = 0; i <= pipeData->child_count; i++) {
        if (pipeData->process_id == i) {
            continue;
        }
        int error = send(self, i, msg);
        if (error == -1) {
            return error;
        }
    }
    return 1;
}

int receive(void *self, local_id from, Message *msg) {
    struct PipeData *pipeData = (struct PipeData *) self;
    int *pipe = pipeData->pipes[pipeData->process_id][from];
    size_t read_bytes = 0;
    while (read_bytes < sizeof(*msg)) {
        size_t read_tmp = read(pipe[0], msg, sizeof(*msg));
        if (read_tmp == -1) {
            return -1;
        }
        if (read_tmp == 0) {
            return 0;
        }
        read_bytes += read_tmp;
    }
    return 1;
}

int receive_any(void *self, Message *msg) {
    struct PipeData *pipeData = (struct PipeData *) self;
    int8_t read_from = pipeData->last_read + 1;
    if (read_from == pipeData->process_id) {
        read_from++;
    }
    if (read_from > pipeData->child_count) {
        return 0;
    }
    pipeData->last_read = read_from;
    int success = receive(self, read_from, msg);
    if (success == 1) {
        return 1;
    }
    return -1;
}
