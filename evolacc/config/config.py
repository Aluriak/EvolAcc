# -*- coding: utf-8 -*-
#########################
#     CONFIGPARSER      #
#########################
"""
This module is here for simplify work of __main__.
This module provide a decorator for docopt module.

Do something like:
    import config 
    configuration = config.generate_from(__doc__)

Then args will be equal to usable dictionnary like object.
In fact, this dictionnary will be a ChainMap that will take 
count, in order, of command-line arguments, configuration file, 
and default values defined in this file.

configparser will also intercept some arguments, like those that 
trigger saving or loading of (non-)existing configurations.
"""


#########################
# IMPORTS               #
#########################
from evolacc.staticgenome   import Genome

from collections import ChainMap
from docopt      import docopt
import importlib
import random
import json
import sys
import os





#########################
# PRE-DECLARATIONS      #
#########################
# package
PKG_NAME = 'evolacc'
# directories and files
DIRCNAME_USER         = 'evolacc/userdata/'
DIRCNAME_USER_GENOMES = DIRCNAME_USER    +'genomes/'
DIRCNAME_USER_FACTORY = DIRCNAME_USER    +'factories/'
FILENAME_CONFIG       = 'data/inputs/config.json'
# configuration keys
UNIVERSE_SIZE   = 'universe_size'
GENOMES_CLASSES = 'genomes'
FACTORY         = 'factory'
CONFIG_FILE     = 'config_file'




#########################
# GENERATE_FROM         #
#########################
def generate_from(docstring):
    """
    Collect information from given docstring,
    configuration file, and default values.
    Generate and return a dict like object
    that have all keys accessibles.
    """
    # CREATE COMMAND LINE ARGUMENTS CONFIGURATION
    config_args = __parse_from_doc(docstring)

    # TODO: CREATE FILE CONFIGURATION
    config_file = __parse_from_file(
        config_args.get(CONFIG_FILE, FILENAME_CONFIG)
    )

    # TODO: CREATE DEFAULT CONFIGURATION
    config_default = __default_configuration()

    # CREATE AND RETURN FINAL CONFIGURATION
    configuration = ChainMap({}, config_args, config_file, config_default)
    return configuration




#########################
# PARSE FROM DOC        #
#########################
def __parse_from_doc(docstring):
    """
    Collect information from docstring with help of docopt
    Return a dictionnary with all interesting options.
    """
    # CREATE COMMAND LINE ARGUMENTS CONFIGURATION
    # Parse args with docopt and keep those are interestings
    args = docopt(docstring)
    config_args = {k.lstrip('-'):v         # don't keep the firsts '-'
                   for k,v in args.items() 
                   if v is not None and k.startswith('-')}

    return __converted(config_args)



#########################
# PARSE FROM FILE       #
#########################
def __parse_from_file(filename=FILENAME_CONFIG):
    """
    Collect information from config file, formatted in json.
    Return a dictionnary with all interesting options.
    Wait optionnaly the config filename.
    NOT IMPLEMENTED
    """
    try:
        with open(filename, 'r') as f:
            payload = json.load(f)
        conf = __converted(payload)
    except FileNotFoundError:
        print('File ' + filename + ' not found !')
        print('Default configuration will be used.')
        conf = {}
    finally:
        return conf




#########################
# DEFAULT CONFIGURATION #
#########################
def __default_configuration():
    """
    Return dict that describes the default configuration.
    """
    # create default classes
    from evolacc.factory import UnitFactory
    from evolacc.action  import Kill as KillAction
    from evolacc.action  import Duplicate as DpltAction
    from evolacc.unit    import Genome
    class CellGenome(Genome):
        """Die, sometimes"""
        def step(self, simulation, coords):
            if random.randint(0, 10) == 0:
                simulation.add(KillAction(coords))
            elif random.randint(0, 11) == 0:
                simulation.add(DpltAction(coords, factory.create(coords)))
    # unit factory: create always a CellGenome
    factory = UnitFactory()
    factory.addUnit([CellGenome])



    #from evolacc.userdata.genomes.conway import GolCell
    return {
        UNIVERSE_SIZE   : [10,10],
        GENOMES_CLASSES : CellGenome,
        FACTORY         : factory,
        CONFIG_FILE     : 'config_file',
    }




#########################
# NORMALIZED            #
#########################
def __normalized(configuration):
    """
    Return a normalized copy of given configuration.
    Converts all fields that required a conversion.
    For example:
        - functions/classes are replaced by their names.
        - non-string objects are converted in string.
    This function is the complementary of __converted, 
    and return a serializable view of given configuration.
    """
    return NotImplemented




#########################
# CONVERTED             #
#########################
def __converted(configuration):
    """
    Return a converted copy of given configuration.
    Converts all fields that required a conversion.
    For example:
        - functions/classes names are imported 
            and replaced by functions/classes themselves.
        - string are converted in integer, float, list…
    This function is the complementary of __normalized,
    and return usable view of given configuration.
    """
    configuration = dict(configuration)
    # universe size must be treat as a list of integer
    if UNIVERSE_SIZE in configuration:
        configuration[UNIVERSE_SIZE] = tuple((
            int(_) for _ in configuration[UNIVERSE_SIZE].split(',')
        ))

    # import users genomes
    if GENOMES_CLASSES in configuration:
        configuration[GENOMES_CLASSES] = __import_user_genomes(
            configuration[GENOMES_CLASSES].split(',')
        )
    return configuration




#########################
# IMPORT USER GENOMES   #
#########################
def __import_user_genomes(genomes):
    """
    Import all genomes from modules in user genomes directory.
    Given genomes must be a list of string that contain name of
    wanted Genome realizations.
    Return a list of class, garanteed Genome realizations. 
    If a class is found multiple times, it will be added multiple times. 
    If a class is not found, no error will be reported.
    If a class is not a Genome subclass, an error will be reported.
    """
    remain_genomes = set(genomes)
    classes = []
    # open python modules in user genomes directory
    # ex: 'evolacc/usergenomes/thing.py' -> 'evolacc.usergenomes.thing'
    modules = (DIRCNAME_USER_GENOMES.replace('/', '.')+os.path.splitext(f)[0] 
               for f in os.listdir(DIRCNAME_USER_GENOMES) 
               if os.path.splitext(f)[1] == '.py' and f != '__init__.py'
              )
    # collect all expected classes in usergenomes list
    for module in modules:
        # import user module
        module = importlib.import_module(module, package=PKG_NAME)
        # collect expected classes
        for attr_name in module.__dict__.keys():
            attr = module.__getattribute__(attr_name)
            if attr_name in genomes:
                remain_genomes.remove(attr_name)
                if issubclass(attr, Genome):
                    classes.append(attr)
                else:
                    print('WARNING: ' + attr_name + ' is not a Genome realization.') # TODO: replace by logging
    # verify and attach collected genomes to args configuration
    assert(all(issubclass(usergenome, Genome) for usergenome in classes)) # TODO: replace by logging
    if len(remain_genomes) > 0:
        # TODO: replace by logging
        print("WARNING: Genomes not found: "
              + ','.join((str(g) for g in remain_genomes))
             )
    return classes




