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
from evolacc.staticgenome import Genome
from evolacc.factory      import UnitFactory
from evolacc.observer     import Observer

from docopt      import docopt
from collections import ChainMap
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
# directories and files names
DIRCNAME_USER         = 'evolacc/userdata/'
DIRCNAME_USER_GENOMES = DIRCNAME_USER    +'genomes/'
DIRCNAME_USER_FACTORY = DIRCNAME_USER    +'factories/'
DIRCNAME_USER_WATCHERS= DIRCNAME_USER    +'watchers/'
FILENAME_CONFIG       = 'data/inputs/config.json'
# configuration keys
UNIVERSE_SIZE   = 'universe_size'
GENOMES_CLASSES = 'genomes'
FACTORY         = 'factory'
WATCHER_CLASSES = 'watchers'
CONFIG_FILE     = 'config_file'
STEPS_AT_START  = 'steps_at_start'
# configuration keys flags
SAVE_CONFIG_FILE= 'save_config'




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

    # CREATE DEFAULT CONFIGURATION
    config_default = __default_configuration()

    # CREATE AND READ FLAGS
    configuration = ChainMap({}, config_args, config_file, config_default)
    if configuration[SAVE_CONFIG_FILE]:
        __save_config_file(dict(configuration))

    # RETURN FINAL CONFIGURATION
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
# SAVE CONFIG FILE      #
#########################
def __save_config_file(configuration):
    """Save given configuration in configuration file in JSON format.
    Filename used is taken from configuration itself.
    First call __normalized() operation of received configuration.
    """
    try:
        with open(configuration[CONFIG_FILE], 'w') as f:
            json.dump(__normalized(configuration), f, 
                      separators=(',', ':'), indent=4)
    except FileNotFoundError:
        print('WARNING: file ' + configuration[CONFIG_FILE] 
              + ' not found. No operation performed.')
    except ValueError:
        print('WARNING: file ' + configuration[CONFIG_FILE] 
              + ' incorrectly formatted. No operation performed.')



#########################
# DEFAULT CONFIGURATION #
#########################
def __default_configuration():
    """
    Return dict that describes the default configuration.
    """
    # create a basic UnitFactory
    from evolacc.factory import FactoryExample

    return {
        UNIVERSE_SIZE   : [10,10],
        GENOMES_CLASSES : [], # no genome
        WATCHER_CLASSES : [], # no watcher
        FACTORY         : FactoryExample(),
        CONFIG_FILE     : FILENAME_CONFIG,
        # FLAGS
        SAVE_CONFIG_FILE: False,
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
    configuration = dict(configuration)
    # universe size must be treat as a list of integer
    if UNIVERSE_SIZE in configuration:
        configuration[UNIVERSE_SIZE] = ','.join((
            str(_) for _ in configuration[UNIVERSE_SIZE]
        ))

    # convert user genomes
    if GENOMES_CLASSES in configuration:
        configuration[GENOMES_CLASSES] = ','.join((
            cls.__name__ for cls in configuration[GENOMES_CLASSES]
        ))

    # convert user factory
    if FACTORY in configuration:
        configuration[FACTORY] = configuration[FACTORY].__class__.__name__

    # convert user watchers
    if WATCHER_CLASSES in configuration:
        configuration[WATCHER_CLASSES] = ','.join((
            cls.__name__ for cls in configuration[WATCHER_CLASSES]
        ))

    # save config flag never saved
    if SAVE_CONFIG_FILE in configuration:
        del configuration[SAVE_CONFIG_FILE]

    # steps number need to be ints
    if STEPS_AT_START in configuration:
        configuration[STEPS_AT_START] = str(configuration[STEPS_AT_START])

    return configuration




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

    # import user factory
    if FACTORY in configuration:
        configuration[FACTORY] = __import_user_factory(
            configuration[FACTORY]
        )

    # steps number need are integers 
    if STEPS_AT_START in configuration:
        configuration[STEPS_AT_START] = int(configuration[STEPS_AT_START])

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



#########################
# IMPORT USER FACTORY   #
#########################
def __import_user_factory(factory_name):
    """
    Import factory from modules in user factories directory.
    Given factory must be a string that contain name of
    wanted UnitFactory realizations.
    Return a class, garanteed UnitFactory realizations. 
    If a class is not found or not a UnitFactory subclass, 
    it raise a warning and use a new UnitFactory intance.
    """
    factory_class = UnitFactory
    # open python modules in user genomes directory
    # ex: 'evolacc/factories/thing.py' -> 'evolacc.factories.thing'
    modules = (DIRCNAME_USER_FACTORY.replace('/', '.')+os.path.splitext(f)[0] 
               for f in os.listdir(DIRCNAME_USER_FACTORY) 
               if os.path.splitext(f)[1] == '.py' and f != '__init__.py'
              )
    # collect all expected classes in usergenomes list
    for module in modules:
        # import user module
        module = importlib.import_module(module, package=PKG_NAME)
        # collect expected classes
        for attr_name in module.__dict__.keys():
            attr = module.__getattribute__(attr_name)
            if attr_name == factory_name:
                if issubclass(attr, UnitFactory):
                    factory_class = attr
                    break # finished !
                else:
                    print('WARNING: ' + attr_name + ' is not a UnitFactory realization.') # TODO: replace by logging
                    factory_class = UnitFactory
        # don't need to continue if factory finded
        if factory_class is not UnitFactory: break
    # return instance of factory class
    return factory_class()




