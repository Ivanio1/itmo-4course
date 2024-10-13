from typing import Tuple


"""Функция поворота квадрата на 90 градусов"""
def rotate_90(row: int, col: int, n: int) -> Tuple[int, int]:
    return col, n - 1 - row

"""Функция поворота квадрата на 180 градусов"""
def rotate_180(row: int, col: int, n: int) -> Tuple[int, int]:
    return n - 1 - row, n - 1 - col

"""Функция поворота квадрата на 270 градусов"""
def rotate_270(row: int, col: int, n: int) -> Tuple[int, int]:
    return n - 1 - col, row

"""Функция поворота ключа на 90 градусов"""
def rotate_key_90(key: list[int], side_len: int) -> list[int]:
    return [get_position(*rotate_90(*get_coordinates(i, side_len), side_len), side_len) for i in key]

"""Функция поворота ключа на 180 градусов"""
def rotate_key_180(key: list[int], side_len: int) -> list[int]:
    return [get_position(*rotate_180(*get_coordinates(i, side_len), side_len), side_len) for i in key]

"""Функция поворота ключа на 270 градусов"""
def rotate_key_270(key: list[int], side_len: int) -> list[int]:
    return [get_position(*rotate_270(*get_coordinates(i, side_len), side_len), side_len) for i in key]

"""Функция вычисления позииции ячейки в квадрате по ее координатам"""
def get_position(row: int, col: int, n: int) -> int:
    return row * n + col


"""Функция вычисления координат ячейки в квадрате по ее позиции"""
def get_coordinates(pos: int, n: int) -> Tuple[int, int]:
    return pos // n, pos % n

"""Функция вычисления позиций поворотов ячейки"""
def find_opposites(side_len: int, window: int) -> list[int]:
    opposites = [window]
    row, col = get_coordinates(window, side_len)
    w1 = get_position(*rotate_90(row, col, side_len), side_len)
    w2 = get_position(*rotate_180(row, col, side_len), side_len)
    w3 = get_position(*rotate_270(row, col, side_len), side_len)
    # Если повороты одинаковые, нет смысла их добавлять (выбранное окно - центр квадрата, размер квадрата нечетный).
    if window != w1:
        opposites += [w1, w2, w3]
    return opposites
