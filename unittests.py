# -*- coding: utf-8 -*-
#########################
#       UNITESTS        #
#########################


#########################
# IMPORTS               #
#########################
import doctest
import os 




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    # GET PYTHON FILES IN EVOLACC REPERTORY
    # get modules paths
    excluded = ['userdata',]
    modules = ('evolacc/'+m for m in os.listdir('evolacc/')
               if not m.startswith('_') and os.path.isdir('evolacc/'+m)
               and m not in excluded
              )
    # get files paths of each module
    files = []
    excluded = []
    for module in modules: # get names formatted like 'evolacc/action'
        filenames = (module+'/'+f for f in os.listdir(module)
                     if not f.startswith('_') and f.endswith('.py')
                     and f not in excluded
                    )
        files.extend(filenames)

    # LAUNCH UNIT TESTS
    for f in files:
        print(f)
        doctest.testfile(f)


