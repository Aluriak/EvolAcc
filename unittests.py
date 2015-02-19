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
    #print('TESTS OF DNA COMPILER…')
    #doctest.testfile('evolacc/dnacompiler/dnacompiler.py')

    print('TESTS OF CONFIG…')
    doctest.testfile('evolacc/config/config.py')

    print('TESTS OF UNIT FACTORY…')
    doctest.testfile('evolacc/factory/unitfactory.py')

    print('TESTS OF PLACING…')
    doctest.testfile('evolacc/placing/placing.py')



    print('END OF UNIT TESTS')



