from evolacc.userdata.simulations.genalg.factory            import Initializer
from evolacc.userdata.simulations.genalg.watcher            import PopViewer
from evolacc.userdata.simulations.genalg.genome             import FunctionSolution
from evolacc.userdata.globals.alterators.genetic_algorithm  import GeneticAlgorithm

from evolacc.config import ALTERATOR_CLASSES, UNIVERSE_SIZE
from evolacc.config import FACTORY_CLASSES, WATCHER_CLASSES, STEPS

from functools import partial
import math



def create_configuration():
    """Must return a configuration"""
    genalg = partial(GeneticAlgorithm,
                     indiv_keeped_per_gen=10,
                     scoring_func=FunctionSolution.scoring,
                     crossing_func=FunctionSolution.crossing,
                     mutation_rate=0.01,
                     nb_parent=2,
                    )
    return {
        UNIVERSE_SIZE    : [50],
        STEPS            : 400,
        FACTORY_CLASSES  : [Initializer],
        WATCHER_CLASSES  : [PopViewer],
        ALTERATOR_CLASSES: [genalg],
    }



