## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

from bitmath.util import full_one_bit_adder


def main():
    print full_one_bit_adder(0, 0, 0)
    print full_one_bit_adder(0, 1, 0)
    print full_one_bit_adder(1, 0, 0)
    print full_one_bit_adder(1, 1, 0)
    print full_one_bit_adder(0, 0, 1)
    print full_one_bit_adder(0, 1, 1)
    print full_one_bit_adder(1, 0, 1)
    print full_one_bit_adder(1, 1, 1)

main()
