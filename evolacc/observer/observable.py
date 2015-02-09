# -*- coding: utf-8 -*-
#########################
#       OBSERVABLE            
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
class Observable:
    """
    Observable according to Observer Pattern.
    Abstract class.
    """
# CONSTRUCTOR #################################################################
    def __init__(self, observers=None):
        self.observers = observers if observers is not None else set()

# PUBLIC METHODS ##############################################################
    def attach_observers(self, observers):
        """add all observer of iterable observers to self"""
        self.observers.extend(observers)

    def notify_observers(self):
        """update all knowed observers"""
        [obs.update() for obs in self.observers]

    def detach_observers(self, observers):
        """retract all observers in given list of self"""
        self.observers = set(self.observers) - set(observers)

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



