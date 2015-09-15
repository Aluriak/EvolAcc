# -*- coding: utf-8 -*-
#########################
#  GENETIC ALGORITHM    #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.alterator import Alterator
from evolacc.action    import ReplaceGeneration
#from queue             import PriorityQueue
import itertools
import random
import heapq
import math



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# GENETIC ALGO CLASS    #
#########################
class GeneticAlgorithm(Alterator):
    """
    Realize a genetic algorithm on simulation.
    The constructor allow to give a lot of parameters.

        indiv_keeped_per_gen: number of individual keeped for doing
            the crossover and generate next population.
        mutation_rate: a value in [0;1] that represent the rate of mutation
            for a Unit.
        scoring_func: a function that returns the score of a unit
        crossing_func: a function that create an iterable of units from nb_parent units
        nb_parent: number of parents involved in the crossover process.

    All units must implements following methods :
        crossover: a callable that take nb_parent Unit
            and return an (iterable of) new Unit.
        mutation: a callable that modify given Unit
        score: a callable that return the score of given Unit
    """

# CONSTRUCTOR #################################################################
    def __init__(self, indiv_keeped_per_gen, mutation_rate,
                 scoring_func, crossing_func,
                 nb_parent=2, parallelization=False):
        """
        All arguments are described in class docstring, or
            parallelization: True iff client want parallelization.
                Its only performed on functions that have an attr
                parallelizable defined and equal to True.

        There is a parallelization iff flag is set to True.

        Because heapq is faster and not thread-safe, information about
        parallelization define which of heapq or PriorityQueue modules is used.
        Heapq module will be used only iff no parallelization is allowed.

        """
        super().__init__()
        # tests
        assert(0.0 <= mutation_rate <= 1.0)
        assert(nb_parent > 0)
        assert(indiv_keeped_per_gen > 0)
        assert(nb_parent <= indiv_keeped_per_gen)
        assert(callable(scoring_func))
        assert(callable(crossing_func))
        # assignations
        if not callable(indiv_keeped_per_gen):  # make it callable
            self.indiv_keeped_per_gen = lambda: indiv_keeped_per_gen
        else:  # indiv_keeped_per_gen is already a callable
            self.indiv_keeped_per_gen = indiv_keeped_per_gen
        self.mutation_rate   = mutation_rate
        self.nb_parent       = nb_parent
        self.parallelization = parallelization
        self.crosses         = crossing_func
        self.scores          = scoring_func
        # not implemented for now
        if self.parallelization is True:
            raise NotImplementedError('parallelization is not implemented now')

# PUBLIC METHODS ##############################################################
    def step(self, simulation):
        """
        """
        if self.parallelization:
            scores = PriorityQueue()
        else:
            scores = []  # heapq works on list

        # SCORING
        def push_unit(coords, unit):
            score = self.scores(unit, simulation)
            if score is not None:
                heapq.heappush(scores, (-score, (coords, unit)))  # heapq manage a minheap
            #else: unit is unscorable, so its untouched by self
        [push_unit(c, u) for c, u in simulation.coords_and_units]

        # KEEP THE FITTEST (bests scores)
        units = tuple(heapq.heappop(scores)
                 for _ in range(self.indiv_keeped_per_gen())
                )

        # CREATE NEW GENERATION THROUGH CROSSINGS
        # Create new units by cross fittest units together
        # define a generator that produces offspring
        def produce_offspring():
            # compute how many offspring are necessary to fill the new population
            offspring_count = simulation.size - len(units)
            while offspring_count > 0:
                # pick random parents of the fittest individuals
                # then create the offsprings
                parents = tuple(p[1] for _, p in random.sample(units, self.nb_parent))
                offspring = self.crosses(parents)
                try:
                    for o in offspring:
                        offspring_count -= 1
                        if offspring_count > 0:
                            yield o
                        else:
                            break
                except TypeError:  # the crossing function returns a unit, not an iterable of unit
                    offspring_count -= 1
                    yield offspring

        new_pop = itertools.chain(
            (
                (unit.mutated(simulation)
                 if   random.random() < self.mutation_rate
                 else unit
                )
                for unit in produce_offspring()
            ),
            # extract the unit from the (-score, (coords, unit)) structure
            (cu[1] for s, cu in units)
        )

        # REPLACE PARENTS BY NEW INDIVS
        simulation.add(
            ReplaceGeneration(new_pop, (c for c, _ in simulation.coords_and_units))
        )




# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



