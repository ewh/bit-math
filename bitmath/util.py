## Copyright (c) 2013 Edward Weston Hunter
## See the file license.txt for copying permission.

from array import array


class ShiftArray(object):
    def __init__(self, n):
        self.n = n
        self._array = array('B', [0] * self.size)
        self.zero_index = 0

    @property
    def size(self):
        return self.n

    @property
    def array(self):
        return self._array

    @property
    def max_index(self):
        return self.size - 1

    def get_actual_index(self, i):
        i = (i + self.zero_index) % self.size
        actual_index = self.max_index - i
        return actual_index

    def get_value(self, i):
        return self.array[self.get_actual_index(i)]

    def set_value(self, i, value):
        self.array[self.get_actual_index(i)] = value

    def left_shift(self, n=1):
        for i in xrange(n):
            self.zero_index = (self.zero_index - 1) % self.size
            self.set_value(0, 0)

    def right_shift(self, n=1):
        for i in xrange(n):
            self.zero_index = (self.zero_index + 1) % self.size
            self.set_value(self.max_index, 0)

    def clone(self, new_length=None):
        if new_length is None:
            new_length = self.size
        new_array = ShiftArray(new_length)
        for i in xrange(min(self.size, new_length)):
            new_array.set_value(i, self.get_value(i))
        return new_array

    def __str__(self):
        import StringIO
        sio = StringIO.StringIO()
        for i in xrange(self.max_index, -1, -1):
            sio.write(str(self.get_value(i)))
        return sio.getvalue()


def full_one_bit_adder(a, b, c):
    sum_out = ((b ^ c) & (not a)) | ((not (b ^ c)) & a)
    c_out = ((a & b) & (not c)) | ((a | b) & c)
    return sum_out, c_out
