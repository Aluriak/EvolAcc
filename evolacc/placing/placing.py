# -*- coding: utf-8 -*-
#########################
#       PLACING         #
#########################
"""

Unit tests:
    >>> from evolacc.placing import Placer
    >>> p = Placer(2)
    >>> _ = [p.place(str((x,y)), (x,y)) for x in range(10) for y in range(10)]
    >>> p.moore_neighbors((3, 3))
    ['(2, 2)', '(2, 3)', '(2, 4)', '(3, 2)', '(3, 4)', '(4, 2)', '(4, 3)', '(4, 4)']
    >>> p.moore_neighbors((0, 3))
    ['(0, 2)', '(0, 4)', '(1, 2)', '(1, 3)', '(1, 4)']
    >>> p.moore_neighbors((0, 0))
    ['(0, 1)', '(1, 0)', '(1, 1)']

"""


#########################
# IMPORTS               #
#########################
from itertools import product



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class Placer(dict):
    """
    Dictionnary and generalist placer of objects in a N-dimensions world.
    Keys are coordinates, and values the object placed at associates coordinates.

    Provide access to neighbors through many methods.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, dimensions=2):
        """Wait for a positiv integer that describes number of dimensions"""
        self.dimensions = dimensions


# PUBLIC METHODS ##############################################################
    def place(self, objct, coords, none_value=None):
        """Place given object in self at given coords
        If another object was at theses coordinates, it will be returned.
        Else, return value is the given none_value (default is None)."""
        assert(self.validate(coords))
        previous = self[coords] if coords in self else none_value
        self[coords] = objct
        return previous

    def moore_neighbors(self, coords):
        """Return list of placed objects that are moore neighbors 
        of given coords.
        """
        assert(self.validate(coords))
        sum_coords = lambda x, y: tuple([a+b for a,b in zip(x, y)])
        # get all exact coords of potential moore_neighbors
        neis = [
            sum_coords(nei_rel_coords, coords)
            for nei_rel_coords in product((-1, 0, 1), repeat=len(coords))
        ]
        # get object for those are defined
        neis = [
            self[nei_coords]
            for nei_coords in neis
            if coords != nei_coords and nei_coords in self
        ]
        return neis


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def validate(self, coords):
        """Return True iff given coords are valid in self"""
        return len(coords) == self.dimensions

    def have(self, coords):
        """Return True iff an object is placed at given coordinates
        TODO: rename this method"""
        return coords in self

# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################


