import unittest
from position import Position
from rotation import Rotation
from orientation import Orientation
from ship import Ship
from board import Board

class TestShip(unittest.TestCase):

    def test_ship_rotate(self):
        '''
        Test ship ends up in correct position after rotation
        '''
        ship = Ship('A', Position(0, 0), Orientation.north)
        ship.rotate(Rotation.right)
        ship.move()
        ship.move()
        position = Position(2, 0)
        self.assertEqual(position, ship.position)

    def test_ship_360_clockwise_rotate(self):
        '''
        Test ship rotates 360 clockwise
        '''
        ship = Ship('A', Position(0, 0), Orientation.north)
        self.assertEqual(Orientation.north, ship.orientation)
        ship.rotate(Rotation.right)
        self.assertEqual(Orientation.east, ship.orientation)
        ship.rotate(Rotation.right)
        self.assertEqual(Orientation.south, ship.orientation)
        ship.rotate(Rotation.right)
        self.assertEqual(Orientation.west, ship.orientation)
        ship.rotate(Rotation.right)
        self.assertEqual(Orientation.north, ship.orientation)

    def test_ship_360_anticlockwise_rotate(self):
        '''
        Test ship rotates 360 anti clockwise
        '''
        ship = Ship('A', Position(0, 0), Orientation.north)
        self.assertEqual(Orientation.north, ship.orientation)
        ship.rotate(Rotation.left)
        self.assertEqual(Orientation.west, ship.orientation)
        ship.rotate(Rotation.left)
        self.assertEqual(Orientation.south, ship.orientation)
        ship.rotate(Rotation.left)
        self.assertEqual(Orientation.east, ship.orientation)
        ship.rotate(Rotation.left)
        self.assertEqual(Orientation.north, ship.orientation)

    def test_ship_move(self):
        '''
        Test ship ends up in correct position after move
        '''
        ship = Ship('A', Position(3, 5), Orientation.west)
        ship.move()
        position = Position(2, 5)
        self.assertEqual(position, ship.position)


    def test_fire(self):
        '''
        Test ship fire missile 
        '''
        ship = Ship('A', Position(0, 0), Orientation.west)
        missiles = ship.missiles - 1
        ship.fire()
        self.assertEqual(ship.missiles, missiles)


class TestBoard(unittest.TestCase):

    def test_board_setup(self):
        '''
        Test ensure 2 ships cannot occupy the same positioon on the grid
        '''
        shipA = Ship('A', Position(0, 0), Orientation.north)
        shipB = Ship('B', Position(0, 0), Orientation.north)
        board = Board(5, [shipA, shipB])
        self.assertEqual(board.get_item(Position(0, 0)), shipA)

    def test_ship_missiles(self):
        '''
        Test ship missiles
        '''
        shipA = Ship('A', Position(0, 0), Orientation.north)
        shipB = Ship('B', Position(0, 1), Orientation.north)
        board = Board(10, [shipA, shipB])
        self.assertEqual(board.get_item(Position(0, 0)), shipA)
        self.assertEqual(board.get_item(Position(0, 1)), shipB)
        board.show_grid()
        board.fire(Position(0, 1))
        self.assertEqual(board.get_item(Position(0, 1)), None)


    def test_ship_missiles_self_destroy(self):
        '''
        Test ship missiles self destory
        '''
        shipA = Ship('A', Position(0, 0), Orientation.west)
        board = Board(2, [shipA])
        self.assertEqual(board.get_item(Position(0, 0)), shipA)
        board.show_grid()
        board.fire(Position(0, 0))
        self.assertEqual(board.get_item(Position(0, 0)), None)
        board.show_grid()

    def test_ship_move(self):
        '''
        Test ship ends up in correct position after move
        '''
        ship = Ship('A', Position(3, 5), Orientation.west)
        ship.move()
        position = Position(2, 5)
        self.assertEqual(position, ship.position)
#

    def test_fire(self):
        '''
        Test ship fire missile 
        '''
        ship = Ship('A', Position(0, 0), Orientation.west)
        missiles = ship.missiles - 1
        ship.fire()
        self.assertEqual(ship.missiles, missiles)


if __name__ == '__main__':
    unittest.main()
