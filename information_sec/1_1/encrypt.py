import random
from typing import Tuple
from transformer import find_opposites, rotate_key_90, rotate_key_180, rotate_key_270


def encrypt_message(text: str) -> Tuple[str, str]:
    square_len = nearest_square_greater_than(len(text))
    print(len(text))
    padded_text = text.ljust(square_len ** 2)
    square = [i for i in range(square_len ** 2)]
    key = []
    # Генерация квадрата Кардано и ключа
    while len(square) != 0:
        empty_cell = random.choice(square)
        key.append(empty_cell)
        windows = find_opposites(square_len, empty_cell)
        for w in windows:
            square.remove(w)

    encrypted = []
    for si in key:
        encrypted.append(padded_text[si])
    for si in rotate_key_90(key, square_len):
        encrypted.append(padded_text[si])
    for si in rotate_key_180(key, square_len):
        encrypted.append(padded_text[si])
    for si in rotate_key_270(key, square_len):
        encrypted.append(padded_text[si])
    return ''.join(encrypted), '-'.join(map(str, key))


def decrypt_message(encrypted: str, key: str) -> str:
    size = int(len(encrypted) ** 0.5)
    key = list(map(int, key.split('-')))
    decrypted = [' '] * (size ** 2)

    quarter = len(encrypted) // 4
    rotations = [
        key,
        rotate_key_90(key, size),
        rotate_key_180(key, size),
        rotate_key_270(key, size)
    ]

    for i, rotation in enumerate(rotations):
        for j, pos in enumerate(rotation):
            decrypted[pos] = encrypted[i * quarter + j]

    return ''.join(decrypted)


def nearest_square_greater_than(size: int) -> int:
    n = 1
    while n ** 2 < size:
        n += 1
    return n
