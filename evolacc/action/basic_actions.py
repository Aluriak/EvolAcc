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
# KILL ACTION           #
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
        assert(simulation.placer.validate(self.coords)) #TODO: replace that by logging
        del simulation.placer[self.coords]

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



