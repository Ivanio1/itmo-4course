from point import Point


class Curve:
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p

    def elliptic_mul(self, p: Point, k):
        """Метод эллиптического умножения"""
        R = p
        for i in range(1, k):
            R = self.elliptic_add(R, p)

        return R

    def elliptic_add(self, P1: Point, P2: Point):
        """Метод эллиптического сложения"""
        x1, y1 = P1.x, P1.y
        x2, y2 = P2.x, P2.y

        if P1 != P2:
            slope = (y2 - y1) * pow(x2 - x1, -1, self.p)
        else:
            slope = (3 * x1 ** 2 + self.a) * pow(2 * y1, -1, self.p)

        x3 = pow(slope * slope - x1 - x2, 1, self.p)
        y3 = pow(slope * (x1 - x3) - y1, 1, self.p)

        return Point(x3, y3)
