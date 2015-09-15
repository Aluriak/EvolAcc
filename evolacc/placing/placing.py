# -*- coding: utf-8 -*-
#########################
#       PLACER          #
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
from functools import lru_cache



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# PLACER CLASS          #
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
        return [
            self[nei_coords]
            for nei_coords in neis
            if coords != nei_coords and nei_coords in self
        ]


# PRIVATE METHODS #############################################################
    @staticmethod
    @lru_cache(maxsize=None)
    def moore_neighbors_offsets(dimensions_count):
        """Return a tuple of moore neighbors offsets, according to given
        dimensions count.

        >>> from evolacc.placing import Placer
        >>> g = Placer.moore_neighbors_offsets(2)
        >>> len(g)
        8
        >>> coords = ((0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,1))
        >>> all(c in g for c in coords)
        True

        """
        # get all exact coords of potential moore_neighbors
        return tuple([
            coords
            for coords in product((-1, 0, 1), repeat=dimensions_count)
            if coords != (0, 0)
        ])

    @staticmethod
    def moore_neighbors_relative(coords):
        """
        Return a generator of coords that are the coordinates of
        moore neighbor of given coords.
        """
        sum_coords = lambda x, y: tuple([a+b for a,b in zip(x, y)])
        # get all exact coords of potential moore_neighbors
        return (
            sum_coords(nei_rel_coords, coords)
            for nei_rel_coords
            in Placer.moore_neighbors_offsets(len(coords))
        )



# PREDICATS ###################################################################
    def validate(self, coords):
        """Return True iff given coords are valid in self"""
        return len(coords) == self.dimensions

    def have(self, coords):
        """Return True iff an object is placed at given coordinates
        TODO: rename this method"""
        return coords in self

# ACCESSORS ###################################################################
    def random_free_moore_neighbor(self, coords):
        """
        return randomly choosed free moore neighbors
        of given coords.
        A moore neighbor is free iff there is no object in.
        Return None if no free moore neighbor found
        """
        assert(self.validate(coords))
        # get object for those are defined
        import random
        neis = [
            nei_coords
            for nei_coords in Placer.moore_neighbors_relative(coords)
            if coords != nei_coords and nei_coords not in self
        ]
        return random.choice(neis) if len(neis) > 0 else None

    def free_moore_neighbor(self, coords):
        """
        return a list of coordinates of free moore neighbors
        of given coords.
        A moore neighbor is free iff there is no object in.
        Return None if no free moore neighbor found
        """
        assert(self.validate(coords))
        # get object for those are defined
        neis = [
            nei_coords
            for nei_coords in Placer.moore_neighbors_relative(coords)
            if coords != nei_coords and nei_coords not in self
        ]
        return random.choice(neis) if len(neis) > 0 else None

    @staticmethod
    def all_coordinates(maximal, dimensions_count=None):
        """Return a generator of all possible coordinates in given conditions.

        If dimensions_count is provided:
            - maximal is an integer value that give the max coordinate in
                a dimnension.
            - dimensions_count is the number of dimensions
        If dimensions_count is not provided:
            maximal is a list of N values, where N is the number
                of dimensions, and each value describes the maximal
                coordinate reachable for one dimension.
        """
        if dimensions_count is None:
            # if all dimensions have the same maximum bound
            if all(m == maximal[0] for m in maximal):
                return Placer.all_coordinates(maximal[0], len(maximal))
            else:
                return NotImplemented
        else:
            return (coords for coords in product(
                range(0, maximal), repeat=dimensions_count
            ))


# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



