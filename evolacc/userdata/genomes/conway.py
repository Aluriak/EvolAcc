# -*- coding: utf-8 -*-
#########################
#       CONWAY          #
#########################
"""
Definition of a StaticGenome realization.
Implements a Conway Game of Life.

Provide an Action realization, GolSwitchState,
that allow cells to switch state when phase is applied.
"""


#########################
# IMPORTS               #
#########################
from evolacc.action       import Action
from evolacc.staticgenome import StaticGenome



#########################
# PRE-DECLARATIONS      #
#########################
class GolSwitchState(Action):
    def __init__(self, coords, new_state):
        self.coords     = coords
        self.new_state  = new_state
    def execute(self, simulation):
        simulation.placer[coords].state = self.new_state



#########################
# LIVE                  #
#########################
class GolCell(StaticGenome):
    """
    Cell of Conway game of life.
    Two states. Rules given in the I/S/B format.
        I = isolement limit
        S = surpopulation limit
        B = born limit
    the Conway Game of Life rules are 2/3/4
    A Cell can have two states : True or False
    """

# CONSTRUCTOR #################################################################
    def __init__(self, I=2, S=3, B=4, state=True):
        self.I, self.S, self.B = I, S, B
        self.state = state


# PUBLIC METHODS ##############################################################
    def step(self, coords, simulation):
        neis = simulation.placer.moore_neighbors(coords)
        # add switch state action to simulation
        simulation.add(GolSwitchState(
            coords, 
            self._next_state((n.state for n in neis))
        ))


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################
    def _next_state(self, neighbors_state):
        """Wait for an iterable of neighbors states (True/False)
        Return the new state of self.
        """
        nb_nei = neighbors_state.count(True)
        if nb_nei <= self.I:
            return False
        if nb_nei >= self.S:
            return False
        if nb_nei >= self.B:
            return True
        return self.state






#########################
# FUNCTIONS             #
#########################



