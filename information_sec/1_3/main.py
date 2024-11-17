from LFSR import LFSR
from io_utils import read_from_file, read_filename


def int_to_seed(number, bit_size) -> list[int]:
    binary_string = bin(number)[2:bit_size + 2]
    binary_string = binary_string.zfill(bit_size)
    seed = [int(bit) for bit in binary_string]
    return seed


seed1 = int_to_seed(3724872364872634, 78)
seed2 = int_to_seed(9284792837542323, 54)
lsfr1 = LFSR(seed1, [75, 6, 3, 1, 0])
lsfr2 = LFSR(seed2, [77, 6, 5, 2, 0])


def transform(text: bytes) -> bytes:
    transformed = []
    for byte in text:
        binary_string = format(byte, '08b')
        for bit in binary_string:
            and_result = lsfr1.data[77] & lsfr2.data[52]
            and_result_2 = lsfr1.data[3] & lsfr2.data[41]

            lsfr1.shift_right()
            lsfr2.shift_right()

            gamma = and_result ^ and_result_2
            transformed.append(int(bit) ^ gamma)
    transformed_text_bytes = [
        int(''.join(map(str, transformed[i:i + 8])), 2) for i
        in range(0, len(transformed), 8)
    ]
    return bytes(transformed_text_bytes)


# input_file = read_filename()
# output_file = read_filename()
# if input_file is not None and output_file is not None:
#     data = read_from_file(input_file)
#     transformed = transform(data)
#     with open(output_file, 'wb') as f:
#         f.write(transformed)
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
data = ''
with open(input_file, 'rb') as f:
    data = f.read()
transformed = transform(data)
with open(output_file, 'wb') as f:
    f.write(transformed)