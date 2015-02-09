# -*- coding: utf-8 -*-
#########################
#       OBSERVER        #
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
class Observer:
    """
    Observer according to Observer Pattern.
    Abstract class.
    """

# CONSTRUCTOR #################################################################
    def __init__(self, observable):
        self.observable = observable

# PUBLIC METHODS ##############################################################
    def initialize(self):
        return NotImplemented

    def update(self):
        return NotImplemented

    def finalize(self):
        return NotImplemented

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



