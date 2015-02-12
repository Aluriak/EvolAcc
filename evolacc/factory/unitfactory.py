# -*- coding: utf-8 -*-
#########################
#     UNITFACTORY       #
#########################
"""
Here is defined a generalist Factory of Unit instances.
User can use UnitFactory class directly or 
subclass it for more complex behaviors.

Unit tests:
    >>> class Property: pass
    >>> from evolacc.unit         import Unit
    >>> from evolacc.staticgenome import StaticGenome
    >>> from evolacc.factory      import UnitFactory
    >>> cpf = [StaticGenome, Property]
    >>> utf = UnitFactory(cpf)
    >>> len(utf.create(42))
    42
    >>> all((isinstance(u, Unit) for u in utf.create(10)))
    True
    >>> all((len(u.components) == len(cpf) for u in utf.create(10)))
    True

"""


#########################
# IMPORTS               #
#########################
from evolacc.unit import Unit, Genome



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
    """


# CONSTRUCTOR #################################################################
    def __init__(self, constructors=[]):
        """Wait for Component constructors that returned 
        one component when called"""
        self.constructors = set(constructors)


# PUBLIC METHODS ##############################################################
    def create(self, count=1):
        """Return list of count new Unit"""
        return [
            Unit(components=(
                constructor() for constructor in self.constructors
            )) 
            for _ in range(count)
        ]

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



