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
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



