from decimal import Decimal


class Binary:
    def __init__(self, binary: str, frac_bit: int = 0):
        if self._validate(binary) is False:
            raise ValueError("Invalid binary")
        self.lBinary = list(binary)
        self.frac_bit = frac_bit
        self._max = 2 ** (len(self.lBinary) - frac_bit) - 1
        self._min = 0

    def __str__(self):  # complete
        binary_str = ''.join(self.lBinary)
        return binary_str[:len(self.lBinary)-self.frac_bit] + "." + binary_str[len(self.lBinary)-self.frac_bit:] + "(2)"

    def __repr__(self):  # complete
        return f"<Binary: {self}>"

    def __eq__(self, other: 'Binary') -> 'Binary':  # complete
        return self.lBinary == other.lBinary

    def __ne__(self, other: 'Binary') -> 'Binary':  # complete
        return self.lBinary != other.lBinary

    def __lt__(self, other: 'Binary') -> 'Binary':  # complete
        return self.__float__() < other.__float__()

    def __le__(self, other: 'Binary') -> 'Binary':  # complete
        return self.__float__() <= other.__float__()

    def __gt__(self, other: 'Binary') -> 'Binary':  # complete
        return self.__float__() > other.__float__()

    def __ge__(self, other: 'Binary') -> 'Binary':  # complete
        return self.__float__() >= other.__float__()

    def __len__(self) -> int:  # complete
        return len(self.lBinary)

    def __int__(self) -> int:  # complete
        return int(self.__float__())

    def __add__(self, other: 'Binary') -> 'Binary':  # complete
        if self.frac_bit != other.frac_bit:
            raise ValueError("Fraction bit is not same")
        copy = self.copy()
        max_len = max(len(copy), len(other)) + 1
        if len(copy) < len(other):
            ex_self = copy._extend(len(other) - len(copy) + 1)
            ex_other = other._extend(1)
        else:
            ex_self = other._extend(len(copy) - len(other) + 1)
            ex_other = copy._extend(1)
        reversed_self = ex_self.lBinary[::-1]
        reversed_other = ex_other.lBinary[::-1]
        carry = 0
        for i in range(max_len):
            sum = int(reversed_self[i]) + int(reversed_other[i]) + carry
            reversed_self[i] = str(sum % 2)
            carry = 1 if sum >= 2 else 0
        copy.lBinary = reversed_self[::-1]
        return copy

    def __lshift__(self, other: int) -> 'Binary':  # complete
        copy = self.copy()
        for _ in range(other):
            copy.lBinary.append('0')
        return copy

    def __rshift__(self, other: int) -> 'Binary':  # complete
        copy = self.copy()
        for _ in range(other):
            copy.lBinary.pop(-1)
        return copy

    def __and__(self, other: 'Binary') -> 'Binary':  # complete
        if len(self.lBinary) != len(other.lBinary):
            raise ValueError("Length of binary is not same")
        copy = self.copy()
        for i in range(len(self.lBinary)):
            copy.lBinary[i] = '1' if self.lBinary[i] == '1' and other.lBinary[i] == '1' else '0'
        return copy

    def __or__(self, other: 'Binary') -> 'Binary':  # complete
        if len(self.lBinary) != len(other.lBinary):
            raise ValueError("Length of binary is not same")
        copy = self.copy()
        for i in range(len(self.lBinary)):
            copy.lBinary[i] = '1' if self.lBinary[i] == '1' or other.lBinary[i] == '1' else '0'
        return copy

    def __xor__(self, other: 'Binary') -> 'Binary':  # complete
        if len(self.lBinary) != len(other.lBinary):
            raise ValueError("Length of binary is not same")
        copy = self.copy()
        for i in range(len(self.lBinary)):
            copy.lBinary[i] = '1' if self.lBinary[i] != other.lBinary[i] else '0'
        return copy

    def __invert__(self):  # complete
        copy = self.copy()
        copy.lBinary = (
            ['1' if b == '0' else '0' for b in self.lBinary])
        return copy

    def _validate(self, binary: str) -> bool:
        return all([b in ['0', '1'] for b in binary])

    @property
    def bin(self):
        return ''.join(self.lBinary)

    @property
    def max(self):
        return self._max

    @property
    def min(self):
        return self._min
