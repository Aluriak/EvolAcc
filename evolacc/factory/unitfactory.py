# -*- coding: utf-8 -*-
#########################
#     UNITFACTORY       #
#########################
"""
Here is defined a generalist Factory of Unit instances.
User can use UnitFactory class directly or 
subclass it for more complex behaviors.
"""


#########################
# IMPORTS               #
#########################
from evolacc.unit import Unit, Genome
import random



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# UNIT FACTORY CLASS    #
#########################
class UnitFactory:
    """
    Factory of Unit instances, based of noparameter functions that returned 
    Component realizations that will be added to each Unit.

    User, when launch simulation, can provide an instance of this class (or 
    any subclass) for get a total control of Simulation initialization.

    At initialization, create() will be called for each place in the 
    Simulation.
    """


# CONSTRUCTOR #################################################################
    def __init__(self):
        pass


# PUBLIC METHODS ##############################################################
    def create(self, simulation, coords):
        """Return a new Unit, choose randomly in knowed ones, and initialize
        with their components.
        Return None by default, and when if no Unit need to be create.
        """
        return None


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# REALIZATION EXAMPLE   #
#########################
from evolacc.action  import Kill as KillAction
from evolacc.action  import Duplicate as DpltAction
class FactoryExample(UnitFactory):
    """
    Basic example of factory that 
    always create the same unit. Yeepie.
    """
    class GenomeExample(Genome):
        """Dies and duplicate, sometimes.
        Its just a basic example. Provided for testing."""
        def step(self, simulation, coords):
            if random.randint(0, 10) == 0:
                simulation.add(KillAction(coords))
            elif random.randint(0, 10) == 0:
                simulation.add(DpltAction(coords, FactoryExample.GenomeExample(None)))
        def __str__(self): return 'X'

    def create(self, simulation, coords):
        return Unit([FactoryExample.GenomeExample(simulation, coords)])


