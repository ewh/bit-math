## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

from util import ShiftArray, full_one_bit_adder


class BinIntException(Exception):
    pass


class Environment(object):
    def __init__(self):
        self.contexts = {}

    def new_int(self, bit_depth, signed):
        pass

    def get_context(self, bit_depth, signed=False):
        context_key = (bit_depth, signed)
        if not self.contexts.has_key(context_key):
            new_context = Context(bit_depth, signed)
            self.contexts[context_key] = new_context


master_context = Environment()


class Context(object):
    def __init__(self, bit_depth, signed=False):
        self.bit_depth = bit_depth
        self.signed = signed
        self._unit = self.new_unit()
        self._neg_unit = self.new_unit(negative=True)

    @property
    def unit(self):
        return self._unit

    @property
    def negative_unit(self):
        return self._neg_unit

    def new_int(self):
        return BinInt(n=self.bit_depth, context=self, signed=self.signed)

    def new_unit(self, negative=False):
        x = self.new_int()
        x.bit_on(0)
        if negative:
            x.negate()
        return x


class BinInt(object):
    def __init__(self, n=None, context=None, signed=False):
        self._array = ShiftArray(n) if n else None
        self._context = context
        self._signed = signed

    @property
    def size(self):
        return self._array.size if self._array else 0

    @property
    def array(self):
        return self._array

    @property
    def max_index(self):
        return self.size - 1

    @property
    def context(self):
        return self._context

    ## Basic Operations

    def get_bit(self, i):
        return self.array.get_value(self.max_index - i)

    def set_bit(self, i, value):
        self.array.set_value(self.max_index - i, value)

    def bit_on(self, i):
        self.set_bit(i, 1)

    def bit_off(self, i):
        self.set_bit(i, 0)

    def all_on(self):
        for i in xrange(self.size):
            self.bit_on(i)

    def all_off(self):
        for i in xrange(self.size):
            self.bit_off(i)

    def clone(self):
        new_binint = BinInt(n=None, context=self._context)
        new_binint._array = self._array.clone()
        return new_binint

    def __str__(self):
        return str(self.array)

    ## Mathematical Operations

    def negate(self):
        raise NotImplementedError

    def is_zero(self):
        zero_result = True
        for i in xrange(self.size):
            if self.get_bit(i) == 1:
                zero_result = False
                break
        return zero_result

    def add(self, other):
        assert self.size == other.size
        adder_carry = 0
        for i in xrange(self.size):
            a_bit = self.get_bit(i)
            b_bit = other.get_bit(i)
            adder_sum, adder_carry = full_one_bit_adder(a_bit, b_bit, adder_carry)
            self.set_bit(i, adder_sum)
            # print i, a_bit, b_bit, adder_sum, adder_carry

    def subtract(self, other):
        raise NotImplementedError

    def multiply(self, other):
        raise NotImplementedError

    def divide(self, other):
        raise NotImplementedError

    def increment(self, other):
        raise NotImplementedError

    def decrement(self, other):
        raise NotImplementedError

    ## Bit Logic Operations

    def invert(self):
        for i in xrange(self.size):
            self.set_bit(i, int(not self.get_bit(i)))

    def bit_and(self, other):
        raise NotImplementedError

    def bit_or(self, other):
        raise NotImplementedError

    def xor(self, other):
        raise NotImplementedError

    def left_shift(self, n=1):
        self.array.left_shift(n)

    def right_shift(self, n=1):
        self.array.right_shift(n)
