# -*- coding: utf-8 -*-
#########################
#       UNIT            #
#########################
"""
A Unit is the very basic unit of something in a Simulation.
Unit a composite of Component instances.
Unit can represent particles of environment or unit of life.
"""


#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class Unit:
    """
    Unit of life/environment.
    Composite of Components.
    """


# CONSTRUCTOR #################################################################
    def __init__(self, components=None):
        """Wait for an iterable of already initialized components
        Initialized with zero components if not provided"""
        self.components = set(components) if components is not None else []


# PUBLIC METHODS ##############################################################
    def step(self, simulation, coords):
        """Call step method of all components"""
        [c.step(simulation, coords) for c in self.components]

    def add(self, component):
        """Add given component to self. Do nothing if already present"""
        self.components.add(component)

    def rmv(self, component):
        """Remove given component to self. Do nothing if absent"""
        self.components.remove(component)


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def is_life(self):
        """Return True iff self have at least a component 
        that answer True to the same question"""
        return any((c.is_life() for c in self.components))

    
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



