class LFSR:
    def __init__(self, seed: list[int], coef: list[int]):
        self.coef = coef
        self.data = seed
    def shift_right(self):
        new_bit = 0
        for coef in self.coef:
            new_bit = new_bit ^ self.data[coef]
        for i in range(0, len(self.data) - 1):
            self.data[i] = self.data[i + 1]
        self.data[len(self.data) - 1] = new_bit