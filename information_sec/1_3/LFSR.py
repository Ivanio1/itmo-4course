class LFSR:
    def __init__(self, seed: list[int], taps: list[int]):
        self.taps = taps
        self.data = seed

    def shift_right(self):
        new_bit = 0
        for tap in self.taps:
            new_bit ^= self.data[tap]
        for i in range(len(self.data) - 1):
            self.data[i] = self.data[i + 1]
        self.data[-1] = new_bit