import math


def ferma_attack(n):
    """Метод для проведения факторизации Ферма"""
    a = math.isqrt(n)
    b2 = a * a - n

    while b2 < 0 or not is_square(b2):
        a += 1
        b2 = a * a - n

    b = math.isqrt(b2)
    p = a + b
    q = a - b

    return p, q


def is_square(x):
    """Метод проверки числа на квадрат"""
    s = int(math.isqrt(x))
    return s * s == x
