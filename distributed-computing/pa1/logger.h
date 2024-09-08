//
// Created by egor on 08.09.24.
//

#ifndef DISTRIBUTED_LAB1_LOGGER_H
#define DISTRIBUTED_LAB1_LOGGER_H

void write_log(int fd, const char *fmt, ...);

void write_log_raw(int fd, const char* text);

void write_console_log(const char *fmt, ...);

void write_console_log_raw(const char* text);

#endif //DISTRIBUTED_LAB1_LOGGER_H
