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

    def get_value(self, i):
        real_index = (i + self.zero_index) % self.size
        return self.array[real_index]

    def set_value(self, i, value):
        real_index = (i + self.zero_index) % self.size
        self.array[real_index] = value

    def left_shift(self, n=1):
        for i in xrange(n):
            self.set_value(0, 0)
            self.zero_index = (self.zero_index + 1) % self.size

    def right_shift(self, n=1):
        for i in xrange(n):
            self.set_value(self.max_index, 0)
            self.zero_index = (self.zero_index - 1) % self.size

    def clone(self):
        new_array = ShiftArray(self.size)
        for i in xrange(self.size):
            new_array.set_value(i, self.get_value(i))
        return new_array

    def __str__(self):
        import StringIO
        sio = StringIO.StringIO()
        for i in xrange(self.size):
            sio.write(str(self.get_value(i)))
        return sio.getvalue()
