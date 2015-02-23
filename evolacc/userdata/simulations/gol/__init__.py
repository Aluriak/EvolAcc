from evolacc.userdata.simulations.gol.factory import GolFactory
from evolacc.userdata.simulations.gol.watcher import GolWatcher

from evolacc.config import UNIVERSE_SIZE, FACTORY_CLASSES, WATCHER_CLASSES, STEPS_AT_START



def create_configuration():
    """Must return a configuration"""
    return {
        UNIVERSE_SIZE  : [20,20],
        STEPS_AT_START : 150,
        FACTORY_CLASSES: [GolFactory],
        WATCHER_CLASSES: [GolWatcher],
    }



