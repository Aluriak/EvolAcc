# -*- coding: utf-8 -*-
#########################
#       MAIN            #
#########################
"""
Example of usecase for EvolAcc class.
"""

#########################
# IMPORTS               #
#########################
#from evolacc import EvolAcc, Unit
import random
from collections import defaultdict

class EvolAcc():
    def __init__(self, world_size):
        self.engine = Engine(world_size)

    def scatter(self, factories):
        assert(sum((c(0, 0) for c in factories.values())) == 1)
        x, y = self.engine.world_size
        for col in range(x):
            for row in range(y):
                unit = random.choice(tuple(factories.keys()))()
                self.engine.add_unit((row, col), unit)

    def run(self, phase_counter):
        [self.engine.step() for _ in range(phase_counter)]

    def __str__(self):
        output = ''
        x, y = self.engine.world_size
        for col in range(x):
            for row in range(y):
                unit = self.engine.units[col, row]
                output += 'X' if is_turned_on(unit) else '.'
            output += '\n'
        return output


class Unit():
    def __init__(self, genome=None, prop=None):
        self.genome = genome
        self.prop   = prop

    def step(self, coords, env):
        return self.genome(coords, env) if self.genome is not None else True


class Property():
    def __init__(self, *args, **kwargs):
        assert(len(args) == 0) # no positionnal parameter expected
        self.values = dict(kwargs) # copy values


class Engine():
    def __init__(self, world_size):
        self.world_size = world_size
        self.units = defaultdict(lambda:Unit())

    def add_unit(self, coords, unit):
        self.units[coords] = unit

    def step(self):
        for coords, unit in list(self.units.items()):
            unit.step(coords, self)
    
    def neighbors_count(self, coords, filter):
        neighbors = lambda x,y: [(x+i, y+j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not(i == j and i == 0)]
        return len([self.units[nei] for nei in neighbors(*coords) if filter(self.units[nei])])



#########################
# PRE-DECLARATIONS      #
#########################
def is_turned_on(unit):
    return unit.genome == turned_on_genome

def turned_on_genome(coords, env):
    """Implementation of Conway Game of Life"""
    if env.neighbors_count(coords, is_turned_on) not in (2, 3):
        env.units[coords].genome = turned_off_genome
    return True

def turned_off_genome(coords, env):
    """Implementation of Conway Game of Life"""
    if env.neighbors_count(coords, is_turned_on) is 3:
        env.units[coords].genome = turned_on_genome
    return True



#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    ea = EvolAcc(world_size=(4, 4))
    factory_property = lambda x: Property(turned_off=x)
    factory_cell_off = lambda: Unit(genome=turned_on_genome,  prop=factory_property(True ))
    factory_cell_on  = lambda: Unit(genome=turned_off_genome, prop=factory_property(False))
    
    # 40% of 'on' cells (alive, in Conway GOF), and 60% of 'off' cells.
    # unused here: see evolacc implementation
    distrib = {factory_cell_on:(lambda _1,_2:0.4), factory_cell_off:(lambda _1,_2:0.6)}
    print(distrib.__class__, distrib)
    ea.scatter(distrib)
    print(ea, '\n')
    ea.run(1)
    print(ea)



