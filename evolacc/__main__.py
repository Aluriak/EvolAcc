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
    __main__.py [--universe_size=COUNT[,COUNT]] [--genomes=TEXT]

Options:
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



