import struct

w = 32  # длина слова в битах
r = 20  # число раундов
b = 16  # длина ключа
P32 = 0xB7E15163
Q32 = 0x9E3779B9
LEFT = "LEFT"
RIGHT = "RIGHT"

"""Функция циклического сдвига"""
def cyclic_shift(x, y, direction):
    y = y % w
    if direction == LEFT:
        return ((x << y) & (2 ** w - 1)) | (x >> (w - y))
    if direction == RIGHT:
        return (x >> y) | ((x << (w - y)) & (2 ** w - 1))


"""Функция подготовки ключа"""
def rc6_key_schedule(key):
    L = [0] * (b // 4)
    for i in range(b - 1, -1, -1):
        L[i // 4] = (L[i // 4] << 8) + key[i]

    S = [P32]
    for i in range(1, 2 * r + 4):
        S.append((S[i - 1] + Q32) % 2 ** w)

    A = 0
    B = 0
    i = 0
    j = 0
    for _ in range(3 * max(b // 4, 2 * r + 4)):
        A = cyclic_shift((S[i] + A + B) % 2 ** w, 3, LEFT)
        S[i] = cyclic_shift((S[i] + A + B) % 2 ** w, 3, LEFT)
        B = cyclic_shift((L[j] + A + B) % 2 ** w, (A + B) % w, LEFT)
        L[j] = cyclic_shift((L[j] + A + B) % 2 ** w, (A + B) % w, LEFT)
        i = (i + 1) % (2 * r + 4)
        j = (j + 1) % (b // 4)
    return S


"""Функция RC6 шифрования"""
def rc6_encrypt(plaintext, S):
    A, B, C, D = struct.unpack('<4I', plaintext)

    B = (B + S[0]) % 2 ** w
    D = (D + S[1]) % 2 ** w

    for i in range(1, r + 1):
        t = cyclic_shift(B * (2 * B + 1) % 2 ** w, 5, LEFT)  # 5 = log2(32)
        u = cyclic_shift(D * (2 * D + 1) % 2 ** w, 5, LEFT)
        A = (cyclic_shift(A ^ t, u, LEFT) + S[2 * i]) % 2 ** w
        C = (cyclic_shift(C ^ u, t, LEFT) + S[2 * i + 1]) % 2 ** w
        A, B, C, D = B, C, D, A
    A = (A + S[2 * r + 2]) % 2 ** w
    C = (C + S[2 * r + 3]) % 2 ** w

    return struct.pack('<4I', A, B, C, D)
