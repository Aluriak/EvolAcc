# -*- coding: utf-8 -*-
"""
"""


#########################
# IMPORTS               #
#########################
import logging
from logging.handlers import RotatingFileHandler
 

FILENAME_LOG = 'data/outputs/evolacc.log'
# create logger 
LOGGER = logging.getLogger()


def init_logging():
    """
    Init logging for evolacc.
    """
    LOGGER.setLevel(logging.DEBUG)
     
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s :: %(levelname)s :: %(message)s'
    )

    # create a handler to file
    file_handler = RotatingFileHandler(
        FILENAME_LOG, # filename
        'a', 1000000, 1 # append, 1 Mo, 1 backup
    )
    # and define its level and formatter
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # other handler that print logs in term 
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
     
    # add handlers to LOGGER
    for handler in (file_handler, stream_handler):
        LOGGER.addHandler(handler)
     

