import sys
import yaml

import alphabet
from curve import Curve
from point import Point


def main():
    curve = Curve(-1, 1, 751)
    g = Point(0, 1)
    if len(sys.argv) < 2:
        print("You must specify the input file path!")
        return

    input_file = None
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-f' and i + 1 < len(sys.argv):
            input_file = sys.argv[i + 1]

    if input_file is None:
        print("You must specify the input file path!")
        return

    # --- Parsing input yaml-file ---------------------
    with open(input_file, 'r') as file:
        file_contents = file.read()

    doc = yaml.safe_load(file_contents)
    bx = doc['Bx']
    by = doc['By']
    pb = Point(bx, by)
    text = doc['T']
    print(f"Pb = {pb}, Message: {text}")

    k = [int(c_k) for c_k in doc['k']]

    res = []
    print("-------------------------------------------------")
    for i, c in enumerate(text):
        a_pm = alphabet.ALPHABET[c]  # get the corresponding point for symbol
        pm = Point(a_pm.x, a_pm.y)
        c_k = k[i]  # get k for current symbol
        kg = curve.elliptic_mul(g, c_k)  # kG = k * G
        kpb = curve.elliptic_mul(pb, c_k)  # kPb = k * Pb
        pmkpb = curve.elliptic_add(kpb, pm)  # Pm + kPb
        print(f"Symbol: '{c}'; k = {c_k}; Pm = {pm}; kPb = {kpb}")
        print(f"Cm = (kG, Pm+kPb) = ({kg}, {pmkpb})")
        print("-------------------------------------------------")
        res.append(kg)
        res.append(pmkpb)

    print(f"Encrypted message: {res}")


if __name__ == "__main__":
    main()
