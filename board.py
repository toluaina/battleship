from rotation import Rotation
from position import Position
from orientation import Orientation

class Board(object):
    ''' Board class representation
    A board is represented by a grid and the positions of items on it.
    '''
    def __init__(self, size, ships):
        self._size = size
        # the grid is an n x n matrix where all values are initialised to None
        # a cell is occupied by a ship if the value is not None.
        # The origin of the grid at 0,0 is at the bottom left corner
        # The grid should not be modified after creation
        self._grid = [[None] * self._size for _ in xrange(self._size)]
        self._ships = ships
        for ship in self._ships:
            self.move_to_position(ship, ship.position)

    def __repr__(self):
        return 'size: %d; ships: %r' % (self._size, self._ships)

    def __str__(self):
        return 'size: %d; ships: %r' % (self._size, self._ships)

    def within_bounds(self, x, y):
        ''' Check if x and y are within the bounds of the grid
    
        :param x: x position
        :type x: `int`
        :param y: y position
        :type y: `int`
        :returns: True or False
        :rtype: `bool`
        '''
        return x >= 0 and x < self._size and y >= 0 and y < self._size

    def can_move(self, ship, position):
        '''        
        Test if we can move a ship to the new position

        :param ship: ship object
        :type ship: `class::ship.Ship`
        :param position: position object
        :type position: `class::position.position`
        :returns: True or False
        :rtype: `bool`
        '''
        if ship.sunk:
            print ('Cannot move sunken ship: %r' % ship)
            return False
        x_offset = self._size - position.x - 1  # translate to bottom left
        if not self.within_bounds(x_offset, position.y):
            print ('Position %r is not within the grid bounds' % position)
            return False
        if self._grid[x_offset][position.y] is not None:
            print ('There is already a ship at position %r' % position)
            return False
        return True

    def move(self, ship):
        '''
        Moves a ship by one grid position if possible

        :param ship: ship to move
        :type ship: `class::ship.Ship`
        '''
        old_position = ship.position
        new_position = ship.position.getPosition(ship.orientation)
        if self.can_move(ship, new_position):
            ship.move()
            self.move_to_position(ship, new_position)
            self.remove_ship(old_position)

    def fire(self, position):
        ''' 
        Fire at ship at position.
        assumption is that we can fire and sink ourself 

        :param position: position of object being fired at
        :type position: `class::position.position`
        '''
        target = self._grid[self._size - position.x - 1][position.y]
        self.remove_ship(position)
        target.sunk = True
        print ('Destroyed ship %r at position %r' % (target, position))

    def remove_ship(self, position):
        ''' Removes a ship from this location

        :param position: position to remove item from
        :type position: `class::position.Position`
        '''
        x_offset = self._size - position.x - 1  # translate to bottom left
        if self._grid[x_offset][position.y] is not None:
            self._grid[x_offset][position.y] = None

    def get_item(self, position):
        '''
        Gets item at position on the grid.
        
        self._grid[0][0]                     # Top Left
        self._grid[0][self.size-1]           # Top Right
        self._grid[self.size-1][0]           # Bottom Left
        self._grid[self.size-1][self.size-1] # Bottom Right

        :param position: position
        :type position: `class::position.Position`
        '''
        x_offset = self._size - position.x - 1  # translate to bottom left
        return self._grid[x_offset][position.y]

    def move_to_position(self, ship, position):
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
        x_offset = self._size - position.x - 1  # translate to bottom left
        # ensure it is within the grid bounds
        if self.within_bounds(x_offset, position.y):
            if self._grid[x_offset][position.y] is None:
                self._grid[x_offset][position.y] = ship
        else:
            print ('Cannot move ship: %r to position %r' % (ship, position))

    def show_grid(self):
        ''' show the state of the grid 
        '''
        s = [[str(e) for e in row] for row in self._grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
