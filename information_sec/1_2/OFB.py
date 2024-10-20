from RC6 import rc6_key_schedule, rc6_encrypt

"""Функция для заполнения текста до нужной длины
   Заполняет числом равным длине финального паддинга"""
def pad(plaintext):
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding


"""Функция для удаления падднига"""
def unpad(padded_plaintext):
    padding_len = padded_plaintext[-1]
    return padded_plaintext[:-padding_len]

"""Функция операции XOR"""
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

"""Функция для шифрования в режиме OFB"""
def rc6_ofb_encrypt(key, iv, plaintext):
    S = rc6_key_schedule(key)
    ciphertext = bytearray()
    feedback = iv
    padded_plaintext = pad(plaintext)

    for i in range(0, len(padded_plaintext), 16):
        keystream = rc6_encrypt(feedback, S)
        block = padded_plaintext[i:i + 16]
        ciphertext_block = xor_bytes(block, keystream)
        ciphertext.extend(ciphertext_block)
        feedback = keystream

    return bytes(ciphertext)

"""Функция для дешифрования в режиме OFB"""
def rc6_ofb_decrypt(key, iv, ciphertext):
    S = rc6_key_schedule(key)
    plaintext = bytearray()
    feedback = iv

    for i in range(0, len(ciphertext), 16):
        keystream = rc6_encrypt(feedback, S)
        block = ciphertext[i:i + 16]
        plaintext_block = xor_bytes(block, keystream)
        plaintext.extend(plaintext_block)
        feedback = keystream

    return unpad(bytes(plaintext))
