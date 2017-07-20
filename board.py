from error import GridOutOfBoundError
from error import ItemInPositionError

class Board(object):
    ''' Board class representation
    A board is represented by a grid and the positions of items on it.
    '''
    def __init__(self, size):
        self._size = size
        # the grid is an n x n matrix where all values are initialised to None
        # a cell is occupied by a ship if the value is not None.
        # The origin of the grid at 0,0 is at the bottom left corner
        # The grid should not be modified after creation
        self._grid = [[None] * self._size for _ in xrange(self._size)]

    def __repr__(self):
        return 'size: %d' % self._size

    def __str__(self):
        return 'size: %d' % self._size

    def within_bounds(self, position):
        ''' Check if x and y are within the bounds of the grid
     
        :param position: position to test
        :type position: `class::position.Position`
        '''
        if (position.x < 0 or position.x > self._size-1 or
            position.y < 0 or position.y > self._size-1):
            raise GridOutOfBoundError('Outofbounds for position %r ' % position)

    def remove(self, position):
        ''' Removes ship from this position
 
        :param position: position to remove ship from
        :type position: `class::position.Position`
        '''
        ship = self.get(position)
        if ship is not None:
            self.set(None, position)
            print ('[Removed: %r from %r]' % (ship, position))

    def get(self, position):
        '''
        Gets ship at position on the grid.
         
        self._grid[0][0]                     # Top Left
        self._grid[0][self.size-1]           # Top Right
        self._grid[self.size-1][0]           # Bottom Left
        self._grid[self.size-1][self.size-1] # Bottom Right
 
        :param position: position
        :type position: `class::position.Position`
        '''
        # translate to bottom left
        return self._grid[self._size-position.y-1][position.x]

    def set(self, ship, position):
        '''
        Move a ship to a position on the grid.
         
        self._grid[0][0]                     # Top Left
        self._grid[0][self.size-1]           # Top Right
        self._grid[self.size-1][0]           # Bottom Left
        self._grid[self.size-1][self.size-1] # Bottom Right
 
        :param ship: ship to move
        :type ship: `class::ship.Ship`
        :param position: position to move to
        :type position: `class::position.Position`
        '''
        # translate to bottom left
        self._grid[self._size-position.y-1][position.x] = ship

    def can_move(self, position):
        '''        
        Test if we can move a ship to the new position

        :param position: position object
        :type position: `class::position.position`
        '''
        self.within_bounds(position)
        if self.get(position) is not None:
            raise ItemInPositionError('Cannot move to pos: %r' % position)

    def move(self, ship, position):
        '''
        Moves a ship by one grid position

        :param ship: ship to move
        :type ship: `class::ship.Ship`
        :param position: new position to move to
        :type position: `class::position.position`
        '''
        self.can_move(position)
        old_position = ship.position
        self.set(ship, position)
        if old_position != position:
            self.remove(old_position)

    def fire(self, position):
        ''' 
        Fire at ship at position.
        assumption is that we can fire and sink ourself 
 
        :param position: position of the target object 
        :type position: `class::position.position`
        '''
        self.within_bounds(position)
        ship = self.get(position)
        if ship is not None:
            self.remove(position)
            ship.sunk = True
            print ('[Destroyed %r at position %r]' % (ship, position))

    def show_grid(self):
        ''' show the state of the grid
        '''
        s = [[str(e) for e in row] for row in self._grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
        print ('-' * 79)

