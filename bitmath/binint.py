## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

from util import ShiftArray, full_one_bit_adder


class BinIntException(Exception):
    pass


class Environment(object):
    def __init__(self):
        self.contexts = {}

    def __str__(self):
        return 'ENV: %s' % map(str, self.contexts.values())

    def new_int(self, bit_depth, signed):
        pass

    def get_context(self, bit_depth, signed=False):
        context_key = (bit_depth, signed)
        if not context_key in self.contexts:
            new_context = Context(self, bit_depth, signed)
            self.contexts[context_key] = new_context
        return self.contexts[context_key]


master_context = Environment()


class Context(object):
    def __init__(self, environment, bit_depth, signed=False):
        self.environment = environment
        self.bit_depth = bit_depth
        self.signed = signed
        self._unit = self.new_unit()
        self._neg_unit = self.new_unit(negative=True)
        self.carry = 0

    @property
    def unit(self):
        return self._unit

    @property
    def negative_unit(self):
        return self._neg_unit

    def __str__(self):
        return 'CTX:%s-%s' % (self.bit_depth, self.signed)

    def new_int(self):
        return BinInt(context=self)

    def new_unit(self, negative=False):
        x = self.new_int()
        x.bit_on(0)
        if negative:
            x.negate_inplace()
        return x


class BinInt(object):
    def __init__(self, context=None, bit_array=None):
        self._context = context
        self._array = bit_array if bit_array else ShiftArray(self.context.bit_depth)

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

    def __str__(self):
        return str(self.array)

    ## Basic Operations

    def get_bit(self, i):
        return self.array.get_value(i)

    def get_bit_inverted(self, i):
        return int(not self.array.get_value(i))

    def set_bit(self, i, value):
        self.array.set_value(i, value)

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

    ## Clone/Copy Operations

    def clone(self):
        return BinInt.copy_primitive_operation(self)
        # return BinInt(context=self._context, bit_array=self._array.clone())

    def copy_from(self, source):
        BinInt.copy_primitive_operation(source, self)

    ## Mathematical Operations

    def is_negative(self):
        return self.get_bit(self.max_index) == 1

    def negate(self, output=None):
        if output is None:
            output = self.clone()
        output.invert_inplace()
        output.increment_inplace()
        return output

    def is_zero(self):
        zero_result = True
        for i in xrange(self.size):
            if self.get_bit(i) == 1:
                zero_result = False
                break
        return zero_result

    def add(self, other, output=None):
        return BinInt.add_primitive_operation(self, other, output=output)

    def subtract(self, other, output=None):
        return BinInt.add_primitive_operation(self, other, output=output, do_subtract=True)

    def multiply(self, other, output=None):
        raise NotImplementedError

    def divide(self, other, output=None):
        raise NotImplementedError

    def increment(self, n=1, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(n):
            output.add_inplace(self.context.unit)
        return output

    def decrement(self, n=1, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(n):
            output.add_inplace(self.context.negative_unit)
        return output

    def abs(self, output=None):
        if output is None:
            output = self.clone()
        if output.is_negative():
            output.negate_inplace()
        return output

    ## Bit Logic Operations

    def invert(self, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(self.size):
            output.set_bit(i, self.get_bit_inverted(i))
        return output

    def logic_and(self, other, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(self.size):
            output.set_bit(i, output.get_bit(i) & other.get_bit(i))
        return output

    def logic_or(self, other, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(self.size):
            output.set_bit(i, output.get_bit(i) | other.get_bit(i))
        return output

    def logic_xor(self, other, output=None):
        if output is None:
            output = self.clone()
        for i in xrange(self.size):
            output.set_bit(i, output.get_bit(i) ^ other.get_bit(i))
        return output

    def left_shift(self, n=1, output=None):
        self.array.left_shift(n)

    def right_shift(self, n=1, output=None):
        self.array.right_shift(n)

    ## In-place Helper Methods

    def invert_inplace(self):
        return self.invert(output=self)

    def negate_inplace(self):
        return self.negate(output=self)

    def increment_inplace(self, n=1):
        return self.increment(n=n, output=self)

    def decrement_inplace(self, n=1):
        return self.decrement(n=n, output=self)

    def add_inplace(self, other):
        return self.add(other, output=self)

    def abs_inplace(self):
        return self.abs(output=self)

    def logic_and_inplace(self, other):
        return self.logic_and(other, output=self)

    def logic_or_inplace(self, other):
        return self.logic_or(other, output=self)

    def logic_xor_inplace(self, other):
        return self.logic_xor(other, output=self)

    ## Static Helper Methods

    @staticmethod
    def copy_primitive_operation(source, target=None):
        if target is None:
            target = BinInt(context=source.context, bit_array=source.array.clone())
        else:
            target._context = source.context
            target._array = source.array.clone()
        return target

    @staticmethod
    def add_primitive_operation(x, y, output=None, do_subtract=False):
        assert x.size == y.size
        if output is None:
            output = x.context.new_int()
        adder_carry = 0
        for i in xrange(x.size):
            a_bit = x.get_bit(i)
            b_bit = y.get_bit(i) if not do_subtract else y.get_bit_inverted(i)
            adder_sum, adder_carry = full_one_bit_adder(a_bit, b_bit, adder_carry)
            output.set_bit(i, adder_sum)
        if do_subtract:
            BinInt.add_primitive_operation(output, x.context.unit, output)
        x.context.carry = adder_carry
        return output
