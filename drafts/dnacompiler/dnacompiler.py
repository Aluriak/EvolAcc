# -*- coding: utf-8 -*-
#########################
#       DNACOMPILER     #
#########################


#########################
# IMPORTS               #
#########################
from math import log, ceil
from collections import defaultdict



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class DNACompiler():
    """


    UNIT TESTS:
        >>> from dnacompiler import DNACompiler
        >>> cc = DNACompiler(alphabet='01', vocabulary=['ha', 'do', 'ken', 'ka', 'me'])
        >>> sorted(cc.tables.items())
        [('000', 'ha'), ('001', 'me'), ('010', 'ken'), ('100', 'do'), ('110', 'ka')]
        >>> cc.compile('000100010110001000001000')
        'hadokenkamehameha'

    """
    # CONSTRUCTOR #################################################################
    def __init__(self, alphabet, vocabulary):
        """"""
        self.alphabet, self.vocabulary = alphabet, vocabulary
        self._initialize()


# PUBLIC METHODS ##############################################################
    def compile(self, source_code, post_treatment=''.join):
        """Return object code"""
        def cutter(seq, block_size):
            for index in range(0, len(seq), block_size):
                yield self._lexems[seq[index:index+block_size]]

        object_code = cutter(source_code, self.lexem_size)
        return object_code if post_treatment is None else post_treatment(object_code)


# PRIVATE METHODS #############################################################
    def _initialize(self):
        """Create"""
        len_alph = len(self.alphabet)
        self.lexem_size = ceil(log(len(self.vocabulary), len_alph))
        # create list of lexems 
        num2alph = lambda x, n: self.alphabet[(x // len_alph**n) % len_alph]
        lexems = [[str(num2alph(x, n)) for n in range(self.lexem_size)] for x in range(len(self.vocabulary))]
        # create dict lexem:word
        self._lexems = defaultdict(str)
        for lexem, word in zip(lexems, self.vocabulary):
            self._lexems[''.join(lexem)] = word



# PREDICATS ###################################################################
# ACCESSORS ###################################################################
    @property
    def tables(self):
        """Return equivalence vocabulary <=> alphabet sequence."""
        return dict(self._lexems)


# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    from random import choice
    alphabet = 'ATGC'
    source_code = ''.join([choice(alphabet) for _ in range(50)])
    cc = DNACompiler(alphabet=alphabet, vocabulary=['ha', 'do', 'ken', 'ka', 'me'])
    print(source_code, '=>', cc.compile(source_code))


