# -*- coding: utf-8 -*-
#########################
#       UNIT            #
#########################


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
    def __init__(self, components=None)
        """Wait for an iterable of already initialized components
        Initialized with zero components if not provided"""
        self.components = set(components) if components is not None else []


# PUBLIC METHODS ##############################################################
    def step(self, simulation):
        """Call step method of all components"""
        [c.step(simulation) for c in self.components]

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



