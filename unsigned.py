from binary import Binary

class Unsigned(Binary):
    def __init__(self, binary: str, frac_bit: int = 0):
        super().__init__(binary, frac_bit=frac_bit)

    def __repr__(self):  # complete
        return f"<Unsigned binary: {self}>"

    def __neg__(self) -> 'Unsigned':  # complete
        copy = super().__invert__() + Unsigned("1", frac_bit=self.frac_bit)
        return copy

    def __abs__(self):  # complete
        copy = self.copy()
        return copy

    def __float__(self) -> float:  # complete
        int_part, frac_part = self._sep()
        decimal = 0
        for i in range(len(int_part)):
            decimal += int(int_part[i]) * 2 ** (len(int_part) - i - 1)
        for i in range(len(frac_part)):
            decimal += int(frac_part[i]) * 2 ** -(i + 1)
        return float(decimal)

    def _sep(self) -> tuple:  # complete
        int_part = self.lBinary[:len(self.lBinary) - self.frac_bit]
        frac_part = self.lBinary[len(self.lBinary) - self.frac_bit:]
        return int_part, frac_part

    def _extend(self, ex_len: int) -> 'Unsigned':  # complete
        copy = self.copy()
        copy.lBinary = ['0'] * ex_len + copy.lBinary
        return copy

    def copy(self) -> 'Unsigned':  # complete
        return Unsigned(''.join(self.lBinary), frac_bit=self.frac_bit)
