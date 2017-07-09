from enum import Enum

class Rotation(Enum):
    ''' Rotation class representation
    Represents the type of rotation - left or right
    '''
    left = 1
    right = 2

    def __str__(self):
        if self == self.left:
            return 'left'
        elif self == self.right:
            return 'right'
