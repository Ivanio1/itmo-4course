cmake_minimum_required(VERSION 3.29)
project(dlab1_fake C)

set(CMAKE_C_STANDARD 99)

add_executable(dlab1_fake logger.c ipc.c main.c)
