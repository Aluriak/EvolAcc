# -*- coding: utf-8 -*-
#########################
#       MAIN            #
#########################
"""
Launching of EvolAcc.
When totally implemented, this launch will heavily use
command line arguments and config files.

It will be the main way to use EvolAcc without GUI.


Usage:
    __main__.py [options] 

Options:
    --universe_size=COUNT[,COUNT]   size of universe in each dimension
    --genomes=NAME[,NAME]           names of Genome classes used
"""

#########################
# IMPORTS               #
#########################
from evolacc.config import UNIVERSE_SIZE
import evolacc.config as config

from evolacc.evolacc import EvolAcc



#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    # PARSE ARGS
    configuration = config.generate_from(__doc__)

    # RUN EVOLACC
    ea = EvolAcc(configuration)
    print('CONFIGURATION DONE !')
    print('NOW START THE SIMULATION…')
    for _ in range(10):
        ea.run()
        ea.debug_print()



