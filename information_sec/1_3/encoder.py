from LFSR import LFSR

INIT_STATE_LFSR1 = '100101111110010000110011001000111001110001111010101101101100101100000110111111'
INIT_STATE_LFSR2 = '100000111111000111100001001010111001010001000110110011'

seed1 = [int(bit) for bit in INIT_STATE_LFSR1]
seed2 = [int(bit) for bit in INIT_STATE_LFSR2]
lfsr1 = LFSR(seed1, [75, 6, 5, 2, 0])
lfsr2 = LFSR(seed2, [53, 6, 2, 1, 0])


def nonlinear_schema(i):
    and_result = lfsr1.data[77] & lfsr2.data[52]
    and_result_2 = lfsr1.data[3] & lfsr2.data[41]
    lfsr1.shift_right()  # Обновляем LFSR1 каждый бит
    if i % 3 == 0:
        lfsr2.shift_right()  # Обновляем LFSR2 каждый третий бит
    return and_result ^ and_result_2


def encode(text: bytes) -> bytes:
    encoded = []
    i = 0
    for byte in text:
        binary_string = format(byte, '08b')
        for bit in binary_string:
            gamma = nonlinear_schema(i)
            encoded.append(int(bit) ^ gamma)
            i += 1
    transformed_text_bytes = [
        int(''.join(map(str, encoded[i:i + 8])), 2) for i
        in range(0, len(encoded), 8)
    ]
    return bytes(transformed_text_bytes)
