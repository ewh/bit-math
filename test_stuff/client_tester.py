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

    i3 = BinInt(8)
    i3.bit_on(0)
    i3.bit_on(1)
    i4 = BinInt(8)
    i4.bit_on(1)
    i4.bit_on(2)
    i4.bit_on(4)
    i5 = i3.clone()
    print
    print i3
    print i4
    i5.add(i4)
    print i5


main()
