# -*- coding: utf-8 -*-
#########################
#       ALTERATOR       #
#########################
"""
Definition of the abstract type Alterator.

An Alterator is added through a Factory to an EvolAcc Simulation.
At each step, before/after all Unit have generated their actions, all Alterators
step() methods are called.
An Alterator receive a reference to the simulation, but, unlike Unit, no coords.
"""

#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# ALTERATOR CLASS       #
#########################
class Alterator:
    """
    Abstract type. Define one abstract method that allow Alterator to be 
    manipulated by Simulation.
    """

# CONSTRUCTOR #################################################################
    def __init__(self, play_first=False):
        """
        play_first can be provided at construction. 
        Default is False : Alterator do step operation after all Unit.
        """
        self.play_first = play_first

# PUBLIC METHODS ##############################################################
    def step(self, simulation):
        """
        Called before or after all Unit have generated their actions.
        """
        raise NotImplementedError

# PRIVATE METHODS #############################################################
# CLASS METHODS ###############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



