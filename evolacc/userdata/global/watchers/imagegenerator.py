# -*- coding: utf-8 -*-
#########################
#    IMAGE GENERATOR    #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.observer import Observer



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# VIDEO CREATOR CLASS   #
#########################
class ImageGenerator(Observer):
    """
    Observer of Simulation.
    At each phase generate a global picture of the Simulation.
    Finalize by create a gif of all images.
    """


# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
    def initialize(self):
        return NotImplemented

    def update(self):
        return NotImplemented

    def finalize(self):
        return NotImplemented

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################


