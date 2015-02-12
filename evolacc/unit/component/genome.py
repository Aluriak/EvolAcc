# -*- coding: utf-8 -*-
#########################
#       GENOME          #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.unit.component import Component



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# GENOME CLASS          #
#########################
class Genome(Component):
    """
    A Genome is something that can add Actions to Simulation.
    Its also a proof of life.

    Its something like an Abstract class, because there is many 
    way to implement that.
    """

# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def is_life(self):
        """Return True""" 
        return True


# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



