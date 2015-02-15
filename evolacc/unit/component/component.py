# -*- coding: utf-8 -*-
#########################
#       COMPONENT       #
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
class Component:
    """
    Abstract class that describes component of a Unit.
    Genome, Property and Quantity are example of Component realizations.
    """

# CONSTRUCTOR #################################################################
    def __init__(self, simulation, coords=None):
        """Get simulation and coords of Unit in it"""
        pass


# PUBLIC METHODS ##############################################################
    def step(self, simulation, coords):
        """Compute next step in simulation.
        Coords are the coords of self in simulation."""
        raise NotImplementedError

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def is_life(self):
        """Return false, because by default 
        a component is not a proof of life"""
        return False


# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



