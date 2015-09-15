# -*- coding: utf-8 -*-
#########################
#       INITIALIZER     #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.userdata.simulations.genalg.genome import FunctionSolution
from evolacc.factory                            import UnitFactory
import random



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# FACTORY CLASS         #
#########################
class Initializer(UnitFactory):
    """
    """
    def create(self, simulation, coords):
        return FunctionSolution(random.random() * 1 - 0.5)

