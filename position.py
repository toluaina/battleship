from orientation import Orientation

class Position():
    ''' Position class representation
    '''
    def __init__(self, x, y):
        '''
        :param x: x coordinate/row number
        :type x: `int`
        :param y: y coordinate/column number
        :type y: `int`
        '''
        self.x = x
        self.y = y

    def __str__(self):
        return '%d:%d' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def getPosition(self, orientation):
        '''Calculate the new position based on the ship's Orientation
        
        :param orientation: orientation to apply
        :type orientation: `class::orientation.Orientation`
        :returns: position
        :rtype: `class::position.Position`
        '''
        if orientation == Orientation.east:
            return Position(self.x + 1, self.y)
        elif orientation == Orientation.west:
            return Position(self.x - 1, self.y)
        elif orientation == Orientation.north:
            return Position(self.x, self.y + 1)
        elif orientation == Orientation.south:
            return Position(self.x, self.y - 1)
