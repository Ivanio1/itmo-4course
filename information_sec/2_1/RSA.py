def decrypt_block(d, c, N):
    """Метод дешифрации блока"""
    return pow(c, d, N)


def find_d_component(e, phi):
    """Метод вычисления параметра закрытого ключа"""
    return pow(e, -1, phi)


def calculate_phi(p, q):
    """Метод вычисления функции Эйлера"""
    return (p - 1) * (q - 1)
