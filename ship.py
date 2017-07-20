from error import SunkShipError
from error import MissileDepletedError
from rotation import getOrientation


def sunken(f, *args, **kwargs):
    def wrapper(*args):
        if args[0].sunk:
            raise SunkShipError('Cannot %s a sunken ship %r' %
                                (f.func_name, args[0]))
        return f(*args, **kwargs)
    return wrapper


class Ship():
    ''' Ship class representation
    '''
    def __init__(self, name, position, orientation, board, missiles=999999):
        self.name = name
        self.position = position
        self.orientation = orientation
        self.missiles = missiles
        self._sunk = False
        self._board = board
        self._board.move(self, position)

    def __str__(self):
        return '%s %r %s %s' % (self.name, self.position, self.orientation,
                                ' (sunk)' if  self.sunk else '')

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Ship):
            return self.name == other.name and self.position == other.position
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @sunken
    def move(self):
        ''' 
        Advance ship by one grid step depending on orientation
        No action if ship has sunk

        :returns: True or False depending on whether the move was successful
        :rtype: `bool`
        '''
        position = self.position.getPosition(self.orientation)
        self._board.move(self, position)
        self.position = position

    @sunken
    def rotate(self, rotation):
        '''
        Rotate the ship to the left or right
        No action if ship has sunk
        '''
        self.orientation = getOrientation(rotation, self.orientation)

    @sunken
    def fire(self, position):
        '''
        Fire the ship's anti-ship missile
        No action if ship has sunk
        '''
        if self.missiles < 0:
            raise MissileDepletedError('Missiles depleted')
        # decrement missile counter
        self.missiles -= 1
        self._board.fire(position)

    @property
    def sunk(self):
        return self._sunk

    @sunk.setter
    def sunk(self, value):
        self._sunk = value


