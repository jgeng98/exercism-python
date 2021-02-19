class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = [None] * capacity
        self._first = self._last = 0

    def increment_mod(self, num):
        return (num + 1) % self._capacity

    def read(self):
        # if buffer is empty:
        if not self._queue[self._first]:
            raise BufferEmptyException("You cannot read from an empty buffer")
        # if buffer only has one element
        if self._first == self._last:
            temp = self._queue[self._first]
            self._queue[self._first] = None
            return temp
        # if buffer has multiple elements
        else:
            temp = self._queue[self._first]
            self._queue[self._first] = None
            self._first = self.increment_mod(self._first)
            return temp

    def write(self, data):
        # if buffer is full:
        if self._queue[self._last] and self.increment_mod(self._last) == self._first:
            raise BufferFullException("You cannot write to a full buffer.")
        # if buffer is not full:
        if self._queue[self._last]:
            self._last = self.increment_mod(self._last)
            self._queue[self._last] = data
        else:
            self._queue[self._last] = data

        return

    def overwrite(self, data):
        # if buffer is full:
        if self.increment_mod(self._last) == self._first:
            self._queue[self._first] = data
            self._first = self.increment_mod(self._first)
            self._last = self.increment_mod(self._last)
        # if buffer is not full:
        else:
            self.write(data)

        return

    def clear(self):
        self.__init__(self._capacity)
