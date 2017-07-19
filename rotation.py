from enum import Enum
from orientation import Orientation

class Rotation(Enum):
    ''' Rotation class representation
    Represents the type of rotation - left or right
    '''
    left = 1
    right = 2

def getOrientation(rotation, orientation):
    '''
    Get Orientation after rotation
     
    :param rotation: rotation to apply
    :type rotation: `class::rotation.Rotation`
    :param orientation: curent orientation
    :type orientation: `class::orientation.Orientation`
    :returns: orientation
    :rtype: `class::orientation.Orientation`
    '''
    if rotation == Rotation.left:
        if orientation == Orientation.east:
            return Orientation.north
        elif orientation == Orientation.west:
            return Orientation.south
        elif orientation == Orientation.north:
            return Orientation.west
        elif orientation == Orientation.south:
            return Orientation.east
    elif rotation == Rotation.right:
        if orientation == Orientation.east:
            return Orientation.south
        elif orientation == Orientation.west:
            return Orientation.north
        elif orientation == Orientation.north:
            return Orientation.east
        elif orientation == Orientation.south:
            return Orientation.west
