from bitmath import BinInt


def main():
    i1 = BinInt(8)
    i1.bit_on(1)
    i1.bit_on(5)
    print i1
    i1.invert()
    print i1
    i1.left_shift(2)
    print i1
    i1.right_shift()
    print i1
    i1.invert()
    print i1
    i2 = i1.clone()

    i1.bit_on(1)
    i2.bit_off(2)
    print
    print i1
    print i2

    i1.all_on()
    i2.all_off()
    print
    print i1
    print i2


main()
