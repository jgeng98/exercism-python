import string
import random


class Robot:

    names = []

    def __init__(self, prev_name=None):
        while True:
            self._name = "".join(
                random.choices(string.ascii_uppercase, k=2)
                + random.choices(string.digits, k=3)
            )
            if not self._name in Robot.names and prev_name != self._name:
                Robot.names.append(self._name)
                break

    def reset(self):
        cur_name = self._name
        Robot.names.remove(self._name)
        self.__init__(cur_name)

    @property
    def name(self):
        return self._name
