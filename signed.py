from binary import Binary

class Signed(Binary):
    def __init__(self, binary: str, frac_bit: int = 0):
        super().__init__(binary, frac_bit=frac_bit)
        self._max = 2 ** (len(self.lBinary) - frac_bit - 1) - 1
        self._min = -2 ** (len(self.lBinary) - frac_bit - 1)

    def __repr__(self):  # complete
        return f"<Signed binary: {self}>"

    def __neg__(self) -> 'Signed':  # complete
        copy = super().__invert__() + Signed("01", frac_bit=self.frac_bit)
        return copy

    def __abs__(self):  # complete
        copy = self.copy()
        if copy._is_minus():
            copy = copy.__neg__()
        return copy

    def __sub__(self, other: 'Signed') -> 'Signed':  # complete
        return self.copy() + (-other.copy())

    def __float__(self) -> float:  # complete
        copy = self.copy()
        sign = -1 if copy._is_minus() else 1
        if copy.lBinary[0] == '1':
            copy = copy.__neg__()
        int_part, frac_part = copy._sep()
        decimal = 0
        for i in range(len(int_part)):
            decimal += int(int_part[i]) * 2 ** (len(int_part) - i - 1)
        for i in range(len(frac_part)):
            decimal += int(frac_part[i]) * 2 ** -(i + 1)
        return float(sign * decimal)

    def _sep(self) -> tuple:  # complete
        int_part = self.lBinary[1:len(self.lBinary) - self.frac_bit]
        frac_part = self.lBinary[len(self.lBinary) - self.frac_bit:]
        return int_part, frac_part

    def _extend(self, ex_len: int) -> 'Signed':  # complete
        copy = self.copy()
        if copy._is_minus():
            copy.lBinary = ['1'] * ex_len + copy.lBinary
        else:
            copy.lBinary = ['0'] * ex_len + copy.lBinary
        return copy

    def copy(self) -> 'Signed':  # complete
        return Signed(''.join(self.lBinary), frac_bit=self.frac_bit)

    def _is_minus(self) -> bool:
        return self.lBinary[0] == '1'
