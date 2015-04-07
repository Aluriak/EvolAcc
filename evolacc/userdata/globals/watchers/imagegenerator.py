# -*- coding: utf-8 -*-
#########################
#    IMAGE GENERATOR    #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.observer import Observer
from evolacc.config   import DIRNAME_OUTPUTS 



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

    Current implementation don't do that. (just dump simulation
    as string in a file.
    """


# CONSTRUCTOR #################################################################
    def __init__(self, simulation, output_filename=None):
        super().__init__(simulation)
        self.output_path = DIRNAME_OUTPUTS+ImageGenerator.__name__+'/'
        if issubclass(output_filename.__class__, str):
            self.output_path += output_filename
        else:
            self.output_path += 'sim'

# PUBLIC METHODS ##############################################################
    def initialize(self):
        with open(self.output_path, 'w') as f:
            pass

    def update(self):
        with open(self.output_path, 'a') as f:
            f.write(str(self.observable) + '\n')

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


