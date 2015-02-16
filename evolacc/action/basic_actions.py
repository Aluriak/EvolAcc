# -*- coding: utf-8 -*-
#########################
#    BASIC ACTION       #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.action.action import Action



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# KILL ACTION           #
#########################
class Kill(Action):
    """
    Action that lead to unit suppression.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, coords):
        """
        coords are coordinates of unit that need to be kill/suppressed.
        """
        self.coords = coords

# PUBLIC METHODS ##############################################################
    def execute(self, simulation):
        """ Delete unit in given simulation """
        assert(simulation.placer.validate(self.coords)) #TODO: replace that by logging
        del simulation.placer[self.coords]



#########################
# DUPLICATE ACTION      #
#########################
class Duplicate(Action):
    """
    Action that lead to unit duplication in a random free moore neighborood.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, coords, new_unit):
        """
        coords are coordinates of unit that need to be duplicate.
        new_unit is the new unit that will be add.
        """
        self.coords = coords
        self.new_unit = new_unit

# PUBLIC METHODS ##############################################################
    def execute(self, simulation):
        """ Duplicate unit in given simulation """
        assert(simulation.placer.validate(self.coords)) #TODO: replace that by logging
        nei = simulation.placer.random_free_moore_neighbor(self.coords)
        if nei is not None: 
            assert(simulation.placer.place(self.new_unit, nei) is None)
        #else: no free neighbor




#########################
# FUNCTOR ACTION        #
#########################
class FunctionCall(Action):
    """
    Action that call given function with given arguments.
    """
    def __init__(self, function, *args, **kwargs):
        assert(callable(function))
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def execute(self, simulation):
        """Execute function"""
        self.function(*self.args, **self.kwargs)



