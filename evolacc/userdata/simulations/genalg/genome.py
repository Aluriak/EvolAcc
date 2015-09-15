# -*- coding: utf-8 -*-
#########################
#       CONWAY          #
#########################
"""
Definition of a StaticGenome realization.
Implements a Conway Game of Life.
"""


#########################
# IMPORTS               #
#########################
from evolacc.staticgenome import StaticGenome
import random
import math



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CELL                  #
#########################
class FunctionSolution(StaticGenome):
    """
    X value for a function
    """
    next_uid = 1

# CONSTRUCTOR #################################################################
    def __init__(self, value):
        """
        """
        self.value = value
        self.uid   = FunctionSolution.next_uid
        # scoring : a value of pi leads to the maximal score
        self.score = -math.cos(self.value)
        FunctionSolution.next_uid += 1


# PUBLIC METHODS ##############################################################
    def step(self, simulation, coords):
        pass  # do nothing

    def mutated(self, simulation):
        self.value += random.random() - 0.5  # add or sub at most 0.5
        return self

# CLASS METHODS ###############################################################
    @staticmethod
    def scoring(unit, simulation):
        return unit.score

    @staticmethod
    def crossing(parents):
        "Choose only one parent, get its value"
        return FunctionSolution(random.choice(parents).value)

# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################






#########################
# FUNCTIONS             #
#########################



