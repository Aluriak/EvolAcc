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
    --factory=NAME                  name of used factory
    --save_config                   save configuration in the config file
    --config_file=FILE              config file
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
    print('CONFIGURATION…')
    ea = EvolAcc(configuration)
    print('DONE !')
    print('START THE SIMULATION…')
    for _ in range(200):
        ea.run()
        ea.debug_print()
    print('DONE !')



