## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

from bitmath import BinInt, Context, Environment


def random_tests():
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

    print
    print 'Test zero:'
    print i2, i2.is_zero()
    print i3, i3.is_zero()
    print i4, i4.is_zero()
    print i5, i5.is_zero()


def environment_tests():
    # env = Environment()
    # print env

    ctx = Context(bit_depth=8)
    x = ctx.new_int()
    x.bit_on(3)
    x.bit_on(1)
    print x
    print x.increment_inplace()
    print x
    x.decrement_inplace(2)
    print x
    y = x.clone()
    y.bit_off(3)
    print y
    y.copy_from(x)
    print y
    print y.invert()
    print y.negate()

    x.increment_inplace()
    z = ctx.new_int()
    z.bit_on(1)
    z.bit_on(0)
    print x, z
    print x.subtract(z)
    t = z.subtract(x)
    print t, t.is_negative(), t.abs()


def main():
    # random_tests()
    environment_tests()

main()
