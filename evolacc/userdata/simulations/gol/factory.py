# -*- coding: utf-8 -*-
#########################
#       GOL             #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.userdata.genomes.gol    import GolCell
from evolacc.factory                 import UnitFactory
from functools                       import partial
import random



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# FACTORY CLASS         #
#########################
class GolFactory(UnitFactory):
    """
    Factory for Create a Game of Life.
    @see GolCell class for ISB factors and API.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, alive_density=0.5, *, I=1, S=4, B=3):
        """Optionnally wait for [0;1] density of alive cells, 
        and for ISB factors"""
        self.alive_density = alive_density
        self.I, self.S, self.B = I, S, B

# PUBLIC METHODS ##############################################################
    def create(self, simulation, coords):
        new_cell = partial(GolCell, self.I, self.S, self.B)
        if self.alive_density < random.random():
            return new_cell(state=GolCell.ALIVE)
        else:
            return new_cell(state=GolCell.DEAD)

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################



#########################
# FUNCTIONS             #
#########################



