import sys

import alphabet
from curve import Curve
from io_utils import print_red, read_config, print_separator
from point import Point


def main():
    curve = Curve(-1, 1, 751)
    g = Point(0, 1)
    if len(sys.argv) < 2:
        print_red("Укажите название файла с параметрами!")
        return

    input_file = None
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-f' and i + 1 < len(sys.argv):
            input_file = sys.argv[i + 1]

    doc = read_config(input_file)
    bx = doc['Bx']
    by = doc['By']
    pb = Point(bx, by)
    text = doc['T']
    print(f"Pb = {pb}, Сообщение: {text}")

    k = [int(c_k) for c_k in doc['k']]

    res = []
    print_separator()
    for i, c in enumerate(text):
        a_pm = alphabet.ALPHABET[c]
        pm = Point(a_pm.x, a_pm.y)
        c_k = k[i]
        kg = curve.elliptic_mul(g, c_k)
        kpb = curve.elliptic_mul(pb, c_k)
        pmkpb = curve.elliptic_add(kpb, pm)
        print(f"Исходный символ: '{c}'; k = {c_k}; Pm = {pm}; kPb = {kpb}")
        print(f"Cm = (kG, Pm+kPb) = ({kg}, {pmkpb})")
        print_separator()
        res.append(kg)
        res.append(pmkpb)

    print(f"Зашифрованное сообщение: {res}")


if __name__ == "__main__":
    main()
