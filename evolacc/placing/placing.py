# -*- coding: utf-8 -*-
#########################
#       PLACING         #
#########################


#########################
# IMPORTS               #
#########################




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


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def validate(self, coords):
        """Return True iff given coords are valid in self"""
        return len(coords) == self.dimensions


# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



