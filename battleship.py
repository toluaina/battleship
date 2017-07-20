import os
import sys
import string

from ship import Ship
from board import Board
from rotation import Rotation
from position import Position
from orientation import Orientation

def main():

    print ('Battleship')

    if len(sys.argv) < 2:
        raise RuntimeError('Wrong number of input arguments')

    if not os.path.exists(sys.argv[1]):
        raise IOError('Could not find input file %s' % sys.argv[1])

    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        data = f.read().splitlines()

    size = 0
    # dictionary of ships where we identify each ship by its name
    # we just use uppercae letters for the names
    ships = {}
    # actions is a list of tuple where the first item of the tuple is the
    # action M, L, R, F  and the second item is the ship or position
    # e.g [('M', ship) ('L', ship) 'R', ship) ('F', position) ]
    actions = []
    orientations = {'E': Orientation.east,
                    'W': Orientation.west,
                    'N': Orientation.north,
                    'S': Orientation.south}

    board = None

    for i, line in enumerate(data):

        if i == 0:

            # first line is the grid size
            try:
                size = int(line)
                # setup the board dimensions
                board = Board(size)
            except TypeError:
                raise

        elif i == 1:

            # this is the list of ships and their initial position
            contents = [e.strip('(),') for e in line.split()]
            n = 3  # each line contains 3 items: x, y, orientation
            for i in xrange(0, len(contents), n):
                x = int(contents[i:i + n][0])
                y = int(contents[i:i + n][1])
                orientation = contents[i:i + n][2]
                # print ('x = %s; y = %d; orientation = %s' % (x, y, orientation))
                position = Position(x, y)
                ship = Ship(string.ascii_uppercase[len(ships) % 26], position,
                            orientations[orientation], board)
                ships[position] = ship

        else:
            # this is an action
            contents = [e.strip('(),') for e in line.split()]
            x = int(contents[0])
            y = int(contents[1])
            position = Position(x, y)

            if 'M' in line or 'R' in line or 'L' in line:
                # this is a move or rotate action
                for action in contents[2]:
                    if action == 'M':
                        actions.append(('M', ships[position]))
                    elif action == 'L':
                        actions.append(('L', ships[position]))
                    elif action == 'R':
                        actions.append(('R', ships[position]))
            else:
                # this is a fire event
                actions.append(('F', position))



    print ('Grid   : %d' % size)
    print ('Ships  : %s' % ships)
    print ('Actions: %s' % actions)

    # show the initial state of the board
    board.show_grid()

    # execute the actions
    for action, ship in actions:
        if action == 'M':
             ship.move()
        if action == 'L':
            ship.rotate(Rotation.left)
        if action == 'R':
            ship.rotate(Rotation.right)
        if action == 'F':
            ships.itervalues().next().fire(ship)

    board.show_grid()

    # show the final state of the board
    board.show_grid()

    # save the state file
    with open('output.txt', 'w') as f:
        for ship in ships.values():
            print ('ship %s %s' % (ship.position, ship.sunk))
            sunk = ' SUNK' if ship.sunk else ''
            f.write('(%d, %d, %s)%s\n' % (ship.position.x, ship.position.y,
                                          str(ship.orientation)[0].upper(),
                                          sunk))


if __name__ == '__main__':
    main()
