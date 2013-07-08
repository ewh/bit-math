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
    env = Environment()

    ctx8 = env.get_context(8)
    env.get_context(16)

    x = ctx8.new_int()
    x.bit_on(3)
    x.bit_on(1)
    print x
    print x.increment_inplace()
    print x.decrement_inplace(2)
    y = x.clone()
    y.bit_on(5)
    print y
    print y.copy_from(x)
    print y.invert()
    print y.negate()
    print y
    print

    x.increment_inplace()
    z = ctx8.new_int()
    z.bit_on(1)
    z.bit_on(0)
    print x, z
    print x.subtract(z)
    t = z.subtract(x)
    print t, t.is_negative(), t.abs()

    x_incremented = x.increment()
    print x, x_incremented, x.logic_or(x_incremented),\
        x.logic_and(x_incremented), x.logic_xor(x_incremented)

    print
    print t
    t2 = t.clone(11)
    print t2
    t2.right_shift()
    print t2
    t2.left_shift()
    print t2
    t2.left_shift(4)
    print t2
    t2.right_shift()
    print t2
    t2.right_shift()
    print t2
    t3 = t.clone(5)
    print t3
    t3.right_shift()
    print t3
    t3.left_shift()
    print t3
    print env


def dump_shift_array(msg_str, array):
    if msg_str == 'l':
        array.left_shift()
    elif msg_str == 'r':
        array.right_shift()
    print msg_str, array, array.zero_index, array.array


def shift_array_tests():
    from bitmath.util import ShiftArray
    a = ShiftArray(8)
    a.set_value(0, 8)
    a.set_value(1, 1)
    a.set_value(3, 2)
    a.set_value(5, 3)
    a.set_value(7, 4)
    dump_shift_array('a', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('r', a)
    dump_shift_array('r', a)
    dump_shift_array('r', a)
    dump_shift_array('r', a)
    dump_shift_array('r', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('l', a)
    dump_shift_array('r', a)
    dump_shift_array('r', a)


def main():
    # random_tests()
    environment_tests()
    # shift_array_tests()

main()
