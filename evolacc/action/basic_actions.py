# -*- coding: utf-8 -*-
#########################
#    BASIC ACTION       #
#########################


#########################
# IMPORTS               #
#########################
from evolac.action.action import Action



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class Kill(Action):
    """
    Action that lead to unit suppression.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, coords):
        """
        coords are coordinates of unit that need to be kill/suppressed.
        """
        self.coords = coords

# PUBLIC METHODS ##############################################################
    def execute(self, simulation):
        """ Delete unit in given simulation """
        assert(self.coords in simulation.placer) #TODO: replace that by logging
        del simulation.placer[self.coords]

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



