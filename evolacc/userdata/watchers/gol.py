# -*- coding: utf-8 -*-
#########################
#       GOL             #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.observer import Observer
from evolacc.config   import UNIVERSE_SIZE



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# VIDEO CREATOR CLASS   #
#########################
class GolWatcher(Observer):
    """
    Observer of Game of Life in 2D space.
    Print each phases in stdin.
    """


# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
    def initialize(self):
        pass # do_nothing

    def update(self):
        nb_row = self.observable.configuration[UNIVERSE_SIZE][0]
        nb_col = self.observable.configuration[UNIVERSE_SIZE][1]
        print(nb_col*'-')
        for i in range(nb_row):
            for j in range(nb_col):
                if self.observable.placer.have((i, j)):
                    print(str(self.observable.placer[i, j]), end='')
                else:
                    print(' ', end='')
            print('')
        print(nb_col*'-' + '\n')

    def finalize(self):
        pass # do_nothing

# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



