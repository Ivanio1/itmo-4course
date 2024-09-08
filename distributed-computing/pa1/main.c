#include "logger.h"
#include "model.h"
#include "ipc.h"
#include "pa1.h"
#include "common.h"
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <stdio.h>

Message createMessage(int16_t type, const char* text) {
    Message message = {
            .s_header = {
                    .s_magic = MESSAGE_MAGIC,
                    .s_payload_len =0,
                    .s_type = type,
            }
    };
    strcpy(message.s_payload, text);
    return message;
}


void close_unused(int32_t process_id, int pipes[11][11][2], int8_t child_count, int pipes_fd) {
    for (int i = 0; i <= child_count; i++) {
        for (int j = 0; j <= child_count; j++) {
            if (i == j) {
                continue;
            }
            if (i == process_id) {
                close(pipes[j][i][1]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[j][i][1], process_id);
            } else if (j == process_id) {
                close(pipes[i][j][0]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[i][j][0], process_id);
            } else {
                close(pipes[i][j][0]);
                close(pipes[j][i][1]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[i][j][0], process_id);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[j][i][1], process_id);
            }
        }
    }
}

int process_child(int32_t process_id, int pipes[11][11][2], pid_t parent_pid, int8_t child_count, int events_fd,
                  int pipes_fd) {
    close_unused(process_id, pipes, child_count, pipes_fd);
    char created_payload[100];
    snprintf(created_payload, 100, log_started_fmt, process_id, getpid(), parent_pid);
    char done_payload[100];
    snprintf(done_payload, 100, log_done_fmt, process_id);
    write_log_raw(events_fd, created_payload);
    struct PipeData pipeData = {
            .process_id = process_id,
            .pipes = pipes,
            .child_count = child_count,
            .last_read = 0
    };
    Message message = createMessage(STARTED, created_payload);
    int sent = send_multicast(&pipeData, &message);
    if (sent != 1) {
        return -1;
    }
    int32_t received_started = 0;
    int32_t received_completed = 0;

    Message *received = malloc(sizeof(Message));
    while (received_started != child_count) {
        receive_any(&pipeData, received);
        if (received->s_header.s_type == STARTED) {
            received_started++;
        }
    }
    write_log(events_fd, log_received_all_started_fmt, process_id);
    write_log_raw(events_fd, done_payload);
    message = createMessage(DONE, done_payload);
    pipeData.last_read = 0;
    pipeData.process_id = process_id;
    send_multicast(&pipeData, &message);
    while (received_completed != child_count) {
        receive_any(&pipeData, received);
        if (received->s_header.s_type == DONE) {
            received_completed++;
        }
    }
    write_log(events_fd, log_received_all_done_fmt, process_id);
    free(received);
    for (int i = 0; i <= child_count; i++) {
        for (int j = 0; j <= child_count; j++) {
            if (i == j) {
                continue;
            }
            if (i == process_id) {
                close(pipes[i][j][0]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[i][j][0], process_id);
            } else if (j == process_id) {
                close(pipes[j][i][1]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[j][i][1], process_id);
            }
        }
    }
    close(events_fd);
    close(pipes_fd);
    return 0;
}

void
process_parent(int process_id, int pipes[11][11][2], int8_t child_count, int ch_pid[10], int events_fd, int pipes_fd) {
    close_unused(process_id, pipes, child_count, pipes_fd);
    Message *received = malloc(sizeof(Message));
    int32_t received_started = 0;
    int32_t received_completed = 0;
    struct PipeData pipeData = {
            .process_id = 0,
            .pipes = pipes,
            .child_count = child_count,
            .last_read = 0
    };
    while (received_started != child_count) {
        receive_any(&pipeData, received);
        char* test = received->s_payload;
        if (received->s_header.s_type == STARTED) {
            received_started++;
        }
    }
    write_log(events_fd, log_received_all_started_fmt, process_id);
    pipeData.last_read = 0;
    while (received_completed != child_count) {
        receive_any(&pipeData, received);
        if (received->s_header.s_type == DONE) {
            received_completed++;
        }
    }
    write_log(events_fd, log_received_all_done_fmt, process_id);
    free(received);
    for (int i = 0; i <= child_count; i++) {
        for (int j = 0; j <= child_count; j++) {
            if (i == j) {
                continue;
            }
            if (i == process_id) {
                close(pipes[i][j][0]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[i][j][0], process_id);
            } else if (j == process_id) {
                close(pipes[j][i][1]);
                write_log(pipes_fd, "pipe %d process %d CLOSED\n", pipes[j][i][1], process_id);
            }
        }
    }

    for (int i = 0; i < child_count; i++) {
        int status;
        waitpid(ch_pid[i], &status, 0);
    }
    close(events_fd);
    close(pipes_fd);
}

int pipes[11][11][2];

int main(int argc, char **argv) {
    int8_t p = 0;
    int32_t process_id = 0;
    pid_t parent_pid = getpid();
    int events_fd = open(events_log, O_WRONLY | O_TRUNC | O_CREAT | O_APPEND, 0666);
    int pipes_fd = open(pipes_log, O_WRONLY | O_TRUNC | O_CREAT | O_APPEND, 0666);
    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-p") == 0 && i + 1 < argc) {
            p = atoi(argv[i + 1]);
        }
    }
    for (int p1 = 0; p1 <= p; ++p1) {
        for (int p2 = 0; p2 <= p; ++p2) {
            if (p1 == p2) {
                continue;
            }
            int pipe_tmp[2];
            if (pipe(pipe_tmp) < 0) {
                return 1;
            }
            write_log(pipes_fd, "pipe %d process %d OPENED\n", pipe_tmp[0], process_id);
            write_log(pipes_fd, "pipe %d process %d OPENED\n", pipe_tmp[1], process_id);
            pipes[p1][p2][0] = pipe_tmp[0];
            pipes[p2][p1][1] = pipe_tmp[1];
        }
    }
    int ch_pids[10];
    for (int i = 1; i <= p; i++) {
        pid_t pid = fork();
        if (pid == 0) {
            //child
            process_id = i;
            return process_child(process_id, pipes, parent_pid, p, events_fd, pipes_fd);
        } else {
            ch_pids[i - 1] = pid;
        }
    }
    process_parent(process_id, pipes, p, ch_pids, events_fd, pipes_fd);
    return 0;
}
