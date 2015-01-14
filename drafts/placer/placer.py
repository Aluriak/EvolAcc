# -*- coding: utf-8 -*-
#########################
#       PLACER          #
#########################


#########################
# IMPORTS               #
#########################
from collections import defaultdict




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class Placer():
    """

    Place objects in a N dimensions world.
    Use of dictionnary.
    Provides accessors on neighbors.

    The more commons dimensions (2 and 3) 
    are buildables from class methods in_x_dimensions

    """


# CONSTRUCTOR #################################################################
    def __init__(self, dimension_count):
        """"""
        self._objects = defaultdict(lambda: None)
        self._N = dimension_count

    @staticmethod
    def in_2_dimensions():
        """Return new Placer initialized for 2 dimensions"""
        return Placer(2)

    @staticmethod
    def in_3_dimensions():
        """Return new Placer initialized for 3 dimensions"""
        return Placer(3)


# PUBLIC METHODS ##############################################################
    def __getitem__(self, coordinates):
        """Return object at given coordinates, or None"""
        assert(len(coordinates) is self._N)
        return self._objects[coordinates]

    def place(self, item, coordinates):
        """"""
        assert(len(coordinates) is self._N)
        assert(self._objects[coordinates] is None)
        self._objects[coordinates] = item

    def move(self, item, directions):
        """"""
        assert(len(directions) is self._N)
        pass #TODO

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
    @property
    def dimensions(self):
        """Return number of dimensions"""
        return self._N


# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    from random import randint as rdnt

    p = Placer.in_3_dimensions()
    mn, mx = 0, 43

    for i in range(10):
        coords = tuple(rdnt(mn, mx) for _ in range(p.dimensions))
        p.place(i, coords)

    for c, o in p._objects.items():
        print(c, o)



