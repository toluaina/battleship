from error import SunkShipError
from error import MissileDepletedError
from rotation import getOrientation

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

    def sunken(self, action):
        if self.sunk:
            raise SunkShipError('Cannot %s a sunk ship %r' % (action, self))

    def move(self):
        ''' 
        Advance ship by one grid step depending on orientation
        No action if ship has sunk

        :returns: True or False depending on whether the move was successful
        :rtype: `bool`
        '''
        self.sunken('move')
        new_position = self.position.getPosition(self.orientation)
        self._board.move(self, new_position, self.position)
        self.position = new_position

    def rotate(self, rotation):
        '''
        Rotate the ship to the left or right
        No action if ship has sunk
        '''
        self.sunken('move')
        self.orientation = getOrientation(rotation, self.orientation)

    def fire(self, position):
        '''
        Fire the ship's anti-ship missile
        No action if ship has sunk
        '''
        self.sunken('move')
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
