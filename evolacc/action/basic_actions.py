# -*- coding: utf-8 -*-
#########################
#    BASIC ACTION       #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.action.action import Action
from evolacc.config        import LOGGER



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# KILL ACTION           #
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
        if simulation.placer.validate(self.coords):
            del simulation.placer[self.coords]
        else:
            LOGGER.error("Coordinates invalids "
                         + str(self.coords)
                         + ". Kill Action is cancelled."
                        )



#########################
# DUPLICATE ACTION      #
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
        if not simulation.storage.validate(self.coords):
            LOGGER.error('Replace Action: Coordinates ' + str(self.coords)
                         + ' are invalid in Simulation ' + str(simulation))
        else:
            nei = simulation.storage.random_free_moore_neighbor(self.coords)
            if nei is not None:
                assert(simulation.storage.place(self.new_unit, nei) is None)
            #else: no free neighbor





#########################
# FUNCTOR ACTION        #
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



#########################
# REPLACE GENERATION    #
#########################
class ReplaceGeneration(Action):
    """
    Action that lead to replace all given units of simulation by given ones.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, new_units, old_units_coords=None):
        """
        new_units is the iterable of new unit that will be add.
        old_units_coords can be None, if undo action is unexpected.
        """
        self.new_units        = new_units
        self.old_units_coords = old_units_coords

# PUBLIC METHODS ##############################################################
    def execute(self, simulation):
        """ Duplicate unit in given simulation """
        for coords, new_unit in zip(self.old_units_coords, self.new_units):
            if simulation.placer.place(new_unit, coords) is None:
                LOGGER.warning('ReplaceGeneration Action: Coordinates '
                               + str(self.old_units_coords)
                               + ' are not occupied')
            #else: it was an ancient unit at given coords



