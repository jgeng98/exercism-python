# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self._direction = direction
        self._x = x
        self._y = y

    @property
    def coordinates(self):
        return (self._x, self._y)

    @property
    def direction(self):
        return self._direction

    def turn_left(self):
        self._direction = (self._direction - 1) % 4

    def turn_right(self):
        self._direction = (self._direction + 1) % 4

    def advance(self):
        if self._direction == 0:
            self._y += 1
        elif self._direction == 1:
            self._x += 1
        elif self._direction == 2:
            self._y -= 1
        else:
            self._x -= 1

    def move(self, directions):
        # loop through directions
        for instruction in directions:
            # if 'L', turn left
            if instruction == "L":
                self.turn_left()
            # if 'R', turn right
            elif instruction == "R":
                self.turn_right()
            # if 'A', go forward one space in current direction
            else:
                self.advance()
