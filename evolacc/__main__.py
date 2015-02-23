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
    -h --help                       print this help
    -v --version                    print version name
    --universe_size=COUNT[,COUNT]   size of universe in each dimension
    --genomes=NAME[,NAME]           names of Genome classes used
    --watchers=NAME[,NAME]          names of Watcher classes to add to simulation
    --factories=NAME[,NAME]         names of used factory classes
    --simulations=NAME[,NAME]       names of simulations that will be launched
    --save_config                   save configuration in the config file
    --config_file=FILE              config file
    --steps_at_start=COUNT          number of phase computed after initialization
"""

#########################
# IMPORTS               #
#########################
from evolacc.evolacc  import EvolAcc
from evolacc.config   import UNIVERSE_SIZE, LOGGER
import evolacc.config as config



#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    # PARSE ARGS
    configuration = config.generate_from(__doc__)

    # RUN EVOLACC
    LOGGER.info('CONFIGURATION…')
    ea = EvolAcc(configuration)
    LOGGER.info('DONE !')

    LOGGER.info('START THE SIMULATION…')
    ea.start()
    LOGGER.info('DONE !')



