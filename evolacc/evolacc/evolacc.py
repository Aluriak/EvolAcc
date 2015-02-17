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
from evolacc.config     import UNIVERSE_SIZE, STEPS_AT_START, WATCHER_CLASSES



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

        # add observers instances to simulation
        self.simulation.attach_observers(
            (o(self.simulation) for o in configuration[WATCHER_CLASSES])
        )

# PUBLIC METHODS ##############################################################
    def run(self, phase_count=1):
        """Go forward phase_count times in the simulation"""
        self.simulation.step(phase_count)

    def start(self):
        """Do requested simulation"""
        for _ in range(self.configuration[STEPS_AT_START]):
            self.run()

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



