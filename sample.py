from unsigned import Unsigned
from signed import Signed

if __name__ == "__main__":
    b1 = Signed("011010111", frac_bit=3)
    b2 = Signed("111011110", frac_bit=3)
    print("bin (@property)\t", b1.bin, b2.bin)
    print("max (@property)\t", b1.max, b2.max)
    print("min (@property)\t", b1.min, b2.min)
    print("__str__\t", b1, b2)  # __str__
    print("__repr__\t", repr(b1), repr(b2))  # __repr__
    print("__and__\t", b1 & b2)  # __and__
    print("__or__\t", b1 | b2)  # __or__
    print("__xor__\t", b1 ^ b2)  # __xor__
    print("__invert__\t", ~b1, ~b2)  # __invert__
    print("__lshift__\t", b1 << 2)  # __lshift__
    print("__rshift__\t", b1 >> 2)  # __rshift__
    print("__int__\t", int(b1), int(b2))  # __int__
    print("__float__\t", float(b1), float(b2))  # __float__
    print("__abs__\t", float(abs(b1)), float(abs(b2)))  # __abs__
    print("__add__\t", float(b1 + b2))  # __add__
    print("__neg__\t", float(-b1))  # __neg__
    print("__sub__\t", float(b1 - b2))  # __sub__
