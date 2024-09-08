//
// Created by egor on 08.09.24.
//
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include "logger.h"


void write_log(int fd, const char *fmt, ...) {

    va_list va;
    va_start(va, fmt);
    char buf[100];
    vsnprintf(buf, 100, fmt, va);
    write(fd, buf, strlen(buf));
    va_end(va);
    fsync(fd);
}

void write_log_raw(int fd, const char* text) {

    write(fd, text, strlen(text));
    fsync(fd);
}
