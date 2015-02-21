# -*- coding: utf-8 -*-
#########################
#       UNITESTS        #
#########################


#########################
# IMPORTS               #
#########################
import doctest




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    doctest.testfile('evolacc/action/action.py')
    doctest.testfile('evolacc/config/config.py')
    doctest.testfile('evolacc/evolacc/evolacc.py')
    doctest.testfile('evolacc/factory/unitfactory.py')
    doctest.testfile('evolacc/observer/observer.py')
    doctest.testfile('evolacc/placing/placing.py')
    doctest.testfile('evolacc/simulation/simulation.py')
    doctest.testfile('evolacc/unit/unit.py')



