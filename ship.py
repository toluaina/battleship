class Ship():
    ''' Ship class representation
    '''

    def __init__(self, name, position, orientation, missiles=999999):
        self.name = name
        self.position = position
        self.orientation = orientation
        self.missiles = missiles
        self._sunk = False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Ship):
            return self.name == other.name and self.position == other.position
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def move(self):
        ''' 
        Advance ship by one grid step depending on orientation
        No action if ship has sunk

        :returns: True or False depending on whether the move was successful
        :rtype: `bool`
        '''
        if self.sunk:
           return False
        self.position = self.position.getPosition(self.orientation)
        return True

    def rotate(self, rotation):
        '''
        Rotate the ship to the left or right
        No action if ship has sunk

        :returns: True or False depending on whether the rotation was successful
        :rtype: `bool`
        '''
        if self.sunk:
           return False
        self.orientation = self.orientation.getOrientation(rotation)
        return True

    def fire(self):
        '''
        Fire the ship's anti-ship missile
        No action if ship has sunk

        :returns: True or False depending on whether the missile trigger was
                successful
        :rtype: `bool`
        '''
        if not self.sunk and self.missiles > 0:
            # decrement missile count
            self.missiles -= 1
            return True
        return False

    @property
    def sunk(self):
        return self._sunk

    @sunk.setter
    def sunk(self, value):
        self._sunk = value
