# -*- coding: utf-8 -*-
#########################
#     UNITFACTORY       #
#########################
"""
Here is defined a generalist Factory of Unit instances.
User can use UnitFactory class directly or 
subclass it for more complex behaviors.

Unit tests:
    >>> from evolacc.unit         import Unit
    >>> from evolacc.staticgenome import StaticGenome
    >>> from evolacc.factory      import UnitFactory
    >>> cmpnt = [StaticGenome, StaticGenome]
    >>> ufact = UnitFactory()
    >>> ufact.addUnit(cmpnt)
    >>> issubclass(ufact.create().__class__, Unit)
    True
    >>> len(ufact.create().components) == len(cmpnt)
    True

"""


#########################
# IMPORTS               #
#########################
from evolacc.unit import Unit, Component
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

    When create() is called, a randomly choosen set of components is used for
    create a new Unit. As create() is called with references to Simulation and
    coords of Unit in it, Components receive these data through construction.
    """


# CONSTRUCTOR #################################################################
    def __init__(self):
        self.units_componants = list()


# PUBLIC METHODS ##############################################################
    def addUnit(self, components):
        """Wait for a list of Component constructors, 
        that wait for two arguments: a Simulation instance and coords in it.

        Declare a constructor of Unit, added to internal list 
        of Unit constructors.
        """
        assert(all(issubclass(c, Component) for c in components))
        self.units_componants.append(components)

    def create(self, simulation=None, coords=None):
        """Return a new Unit, choose randomly in knowed ones, and initialize
        with their components."""
        assert(len(self.units_componants) > 0)
        return Unit(components=(
            constructor(simulation, coords) for constructor in random.choice(self.units_componants)
        )) 


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



