from util import ShiftArray


class BinIntException(Exception):
    pass


class MasterContext(object):
    pass


class Context(object):
    pass


class BinInt(object):
    def __init__(self, n=None, context=None):
        self._array = ShiftArray(n) if n else None
        self._context = context

    @property
    def size(self):
        return self._array.size if self._array else 0

    @property
    def array(self):
        return self._array

    @property
    def max_index(self):
        return self.size - 1

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

    def negate(self, result=None):
        pass

    def add(self, other, result=None):
        pass

    def subtract(self, other, result=None):
        pass

    def multiply(self, other, result=None):
        pass

    def divide(self, other, result=None):
        pass

    ## Bit Logic Operations

    def invert(self):
        for i in xrange(self.size):
            self.set_bit(i, int(not self.get_bit(i)))

    def bit_and(self, other, result=None):
        pass

    def bit_or(self, other, result=None):
        pass

    def xor(self, other, result=None):
        pass

    def left_shift(self, n=1):
        self.array.left_shift(n)

    def right_shift(self, n=1):
        self.array.right_shift(n)
