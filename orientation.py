from enum import Enum
from rotation import Rotation

class Orientation(Enum):
    ''' Orientation class representation
    '''
    east = 1
    west = 2
    north = 3
    south = 4

    def getOrientation(self, rotation):
        '''
        Get Orientation after rotation
        
        :param rotation: rotation to apply
        :type rotation: `class::rotation.Rotation`
        :returns: orientation
        :rtype: `class::orientation.Orientation`
        '''
        if rotation == Rotation.left:
            if self == self.east:
                return self.north
            elif self == self.west:
                return self.south
            elif self == self.north:
                return self.west
            elif self == self.south:
                return self.east
        elif rotation == Rotation.right:
            if self == self.east:
                return self.south
            elif self == self.west:
                return self.north
            elif self == self.north:
                return self.east
            elif self == self.south:
                return self.west

    def __str__(self):
        if self == self.east:
            return 'east'
        elif self == self.west:
            return 'west'
        elif self == self.north:
            return 'north'
        elif self == self.south:
            return 'south'
