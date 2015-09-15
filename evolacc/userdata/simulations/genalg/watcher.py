# -*- coding: utf-8 -*-
#########################
#       POP VIEWER      #
#########################


#########################
# IMPORTS               #
#########################
from evolacc.observer import Observer
from evolacc.config   import UNIVERSE_SIZE

import math
import statistics as stats


#########################
# PRE-DECLARATIONS      #
#########################


#########################
# VIDEO CREATOR CLASS   #
#########################
class PopViewer(Observer):
    """
    Observer of function solution.
    """

    def update(self):
        values  = [u.value for u in self.observable.units]
        mean    = stats.mean(values)
        max_gen = max(self.observable.units, key=lambda x: x.score)
        print('POPVIEWER:', self.observable.size, '\tAv Score:',
              round(mean, 2),
              '  \tMedian:', round(stats.median(values), 2),
              '  \tStddev:', round(stats.stdev(values, xbar=mean), 2),
              '  \tMax score:', round(max_gen.value, 2), ':', round(max_gen.score, 2),
             )

