# -*- coding: utf-8 -*-
#########################
#       EVOLACC         #
#########################
"""
Main user-interface object of EvolAcc.
"""

#########################
# IMPORTS               #
#########################
from evolacc.simulation import Simulation
from evolacc.config     import UNIVERSE_SIZE



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class EvolAcc:
    """
    Currently, EvolAcc can only do only one simulation.
    """


# CONSTRUCTOR #################################################################
    def __init__(self, configuration):
        print('configuration:', dict(configuration))
        self.simulation = Simulation(configuration)



# PUBLIC METHODS ##############################################################
    def debug_print(self):
        nb_row = self.configuration[UNIVERSE_SIZE][0]
        nb_col = self.configuration[UNIVERSE_SIZE][1]
        print(nb_col*'-')
        for i in range(nb_row):
            for j in range(nb_col):
                if self.simulation.placer.have((i, j)):
                    print(str(self.simulation.placer[i, j]), end='')
                else:
                    print(' ', end='')
            print('')
        print(nb_col*'-' + '\n')

    def run(self, phase_count=1):
        """Go forward phase_count times in the simulation"""
        self.simulation.step(phase_count)


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
    @property
    def configuration(self):
        """Return configuration"""
        return self.simulation.configuration

# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



