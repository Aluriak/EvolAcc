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
from evolacc.action       import FunctionCall
from evolacc.staticgenome import StaticGenome



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CELL                  #
#########################
class GolCell(StaticGenome):
    """
    Cell of Conway game of life.
    Two states. Rules given in the I/S/B format.
        I = isolement limit
        S = surpopulation limit
        B = born limit
    the Conway Game of Life rules are 2/4/3
    A Cell can have two states : True or False
    """
    ALIVE = True
    DEAD  = False

# CONSTRUCTOR #################################################################
    def __init__(self, I=1, S=4, B=3, state=ALIVE):
        assert(state in (GolCell.ALIVE, GolCell.DEAD))
        self.I, self.S, self.B = I, S, B
        self.state = state


# PUBLIC METHODS ##############################################################
    def switch_state(self):
        self.state = not self.state

    def step(self, simulation, coords):
        neis = simulation.placer.moore_neighbors(coords)
        # add switch state action to simulation if necessary
        if self._next_state([n.state for n in neis]) != self.state:
            simulation.add(FunctionCall(
                GolCell.switch_state,
                self
            ))


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
    def __str__(self):
        return 'X' if self.state == GolCell.ALIVE else ' ' 

# OPERATORS ###################################################################
    def _next_state(self, neighbors_state):
        """Wait for an iterable of neighbors states (alive/dead)
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



