# -*- coding: utf-8 -*-
#########################
#       DNACOMPILER     #
#########################


#########################
# IMPORTS               #
#########################
from   math import log, ceil
from   itertools import zip_longest
from   functools import partial, lru_cache
import itertools
import re




#########################
# PRE-DECLARATIONS      #
#########################
# lexems seens in structure
LEXEM_TYPE_CONDITION = 'C'
LEXEM_TYPE_ACTION    = 'A'
LEXEM_TYPE_PREDICAT  = 'P'
LEXEM_TYPE_DOWNLEVEL = 'D'
# lexems only seen in values
LEXEM_TYPE_COMPARISON   = 'C'
LEXEM_TYPE_OPERATOR     = 'O'



#########################
# DNACOMPILER CLASS     #
#########################
class DNACompiler():
    """
    Compiler of code write with any vocabulary. ('01', 'ATGC', 'whatevr',…)
    A source code is an ordered list of vocabulary elements 
        ('10011010000101', 'AGGATGATCAGATA', 'wtrvwhttera'…).
    The source code is readed by following this format:

        ....|......................|............................
        HEAD      STRUCTURE                  VALUES

    The HEAD defines:
        - where STRUCTURE and VALUES start in the code (two integer):
        - where STRUCTURE and VALUES stop  in the code (two integer):
    The STRUCTURE defines:
        - logic of the code;
        - lexems type that will be used;
    The VALUES defines:
        - what are the exact value of each lexem;

    Example of STRUCTURE:
    "
        if C:
            A
            if C:
                A
                A
                if P and P:
                    A
                    A
                A
            if P:
                A
    "
    VALUES will describes which is the value effectively used for each
    lexem, C, A or P. (condition, action, predicat)
    NB: D is the char that indicate a indent level decrease


    UNIT TESTS:
        >>> from dnacompiler import DNACompiler


    """
# CONSTRUCTOR #################################################################
    def __init__(self, alphabet, voc_structure, voc_values):
        """"""
        self.alphabet = alphabet
        self.voc_structure, self.voc_values = vocabulary_struct, voc_values
        self._initialize_tables()
        print(self.table_struct)
        print(self.table_values)


# PUBLIC METHODS ##############################################################
    def compile(self, source_code, post_treatment=''.join):
        """Return object code"""
        # define size of an integer and four of them in the HEADER
        integer_size = self._integer_size_lookup(len(source_code))
        slices = (
            # bound start  , bound end     , step
            (0             , integer_size*1,  1),
            (integer_size*1, integer_size*2,  1),
            (integer_size*2, integer_size*1, -1),
            (integer_size*1, 0             , -1),

        )
        integers = []
        for slice_beg, slice_end, step in slices:
            integer = self.string_to_int(source_code[slice_beg:slice_end:step])
            integers.append(integer % len(source_code))
        # associate each integer as a bound of STRUCTURE and VALUES
        integers.sort()
        print(integers)
        struct_bounds_beg, struct_bounds_end = integers[0], integers[1]
        values_bounds_beg, values_bounds_end = integers[2], integers[3]
        # read structure
        structure = self._structure(
            source_code[struct_bounds_beg:struct_bounds_end]
        )
        print(DNACompiler.prettify_struct(structure))
        # read values
        print(self._struct_to_values(structure, source_code))
        obj_code = self._pythonized(
            structure, self._struct_to_values(
                structure, source_code[values_bounds_beg:values_bounds_end]
            )
        )
        # apply post treatment and return
        return obj_code if post_treatment is None else post_treatment(obj_code)


# PRIVATE METHODS #############################################################
    def _initialize_tables(self):
        """Create tables for structure and values, word->vocabulary"""
        # structure table
        self.table_struct, self.idnt_struct_size = DNACompiler.create_struct_table(
            self.alphabet, self.voc_structure
        )
        # values table
        self.table_values, self.idnt_values_size = DNACompiler.create_values_table(
            self.alphabet, self.voc_values
        )

    def _structure(self, source_code):
        """return structure in ACDP format."""
        # define cutter as a per block reader
        def cutter(seq, block_size):
            for index in range(0, len(seq), block_size):
                lexem = seq[index:index+block_size]
                if len(lexem) == block_size:
                    yield self.table_struct[seq[index:index+block_size]]
        return tuple(cutter(source_code, self.idnt_struct_size))

    def _pythonized(self, structure, values):
        """Return python code associated to given structure and values"""
        print('SOURCE:', structure, values)
        python_code = ""
        stack = []
        push = lambda x: stack.append(x)
        pop  = lambda  : stack.pop()
        last = lambda  : stack[-1] if len(stack) > 0 else ' '
        def indented_code(s, level):
            return '\t'*level + s + '\n'

        level = 0
        CONDITIONS = [LEXEM_TYPE_PREDICAT, LEXEM_TYPE_CONDITION]
        ACTION = LEXEM_TYPE_ACTION
        DOWNLEVEL = LEXEM_TYPE_DOWNLEVEL
        for lexem_type in structure:
            if lexem_type is ACTION:
                if last() in CONDITIONS:
                    value, values = values[0:len(stack)], values[len(stack):]
                    python_code += indented_code('if ' + ' and '.join(value) + ':', level)
                    stack = []
                    level += 1
                python_code += indented_code(values[0], level)
                values = values[1:]
            elif lexem_type in CONDITIONS:
                push(lexem_type)
            elif lexem_type is DOWNLEVEL:
                level = max(level-1, 0)
        return python_code

    def _struct_to_values(self, structure, source_code):
        """Return list of values readed in source_code, 
        according to given structure.
        """
        # iterate on source_code until all values are finded
        iter_source_code = itertools.cycle(source_code)
        values = []
        for lexem_type in (l for l in structure if l is not 'D'):
            if lexem_type is LEXEM_TYPE_CONDITION:
                values.append(self.next_condition_lexems(
                    iter_source_code
                ))
            else:
                values.append(self.next_lexem(
                    lexem_type, iter_source_code
                ))

        return values

    def next_lexem(self, lexem_type, source_code):
        """Return next readable lexem of given type in source_code"""
        # define reader as a lexem extractor
        def reader(seq, block_size):
            identificator = ''
            for char in source_code:
                identificator += char
                if len(identificator) == self.idnt_values_size:
                    #print(identificator, lexem_type)
                    yield self.table_values[lexem_type][identificator]
                    identificator = ''
        lexem_reader = reader(source_code, self.idnt_values_size)
        lexem = None
        while lexem is None: lexem = next(lexem_reader)
        # here we have found a lexem
        return lexem
        
    def next_condition_lexems(self, source_code):
        """Return condition lexem readed in source_code"""
        # find three lexems
        lvl = self.next_lexem(LEXEM_TYPE_COMPARISON, source_code)
        loc = self.next_lexem(LEXEM_TYPE_OPERATOR  , source_code)
        lvr = self.next_lexem(LEXEM_TYPE_COMPARISON, source_code)
        # here we have found a lexem
        return ' '.join((lvl, loc, lvr))
        


    @lru_cache(maxsize = 100)
    def string_to_int(self, s):
        """Read an integer in s, in Little Indian. """
        base = len(self.alphabet)
        return sum((self.letter_to_int(l) * base**lsb 
                    for lsb, l in enumerate(s)
                   ))

    @lru_cache(maxsize = None)
    def letter_to_int(self, l):
        return self.alphabet.index(l)


    def _integer_size_lookup(self, source_code_size):
        """Find and return the optimal integer size.
        A perfect integer can address all indexes of 
        a string of size source_code_size.
        """
        return ceil(log(source_code_size, len(self.alphabet)))

        



# CLASS METHODS ###############################################################
    @staticmethod
    def create_struct_table(alphabet, vocabulary):
        """Create table identificator->vocabulary, 
        and return it with size of an identificator"""
        len_alph = len(alphabet)
        identificator_size = ceil(log(len(vocabulary), len_alph))
        # create list of lexems 
        num2alph = lambda x, n: alphabet[(x // len_alph**n) % len_alph]
        identificators = [[str(num2alph(x, n)) 
                           for n in range(identificator_size)
                          ] 
                          for x in range(len(vocabulary))
                         ]
        # create dict identificator:word
        identificators_table = {}
        zip_id_voc = zip_longest(identificators, vocabulary, fillvalue=None)
        for idt, word in zip_id_voc:
            identificators_table[''.join(idt)] = word
        return identificators_table, identificator_size


    @staticmethod
    def create_values_table(alphabet, vocabulary):
        """Create table lexem_type->[identificator->vocabulary], 
        and return it with size of a lexem"""
        len_alph = len(alphabet)
        identificator_size = ceil(log(len(vocabulary), len_alph))
        # create list of lexems 
        num2alph = lambda x, n: alphabet[(x // len_alph**n) % len_alph]
        identificators = [[str(num2alph(x, n)) 
                           for n in range(identificator_size)
                          ] 
                          for x in range(len(vocabulary))
                         ]
        # create dict identificator:word
        identificators_table = {}
        zip_voc = partial(zip_longest, identificators, fillvalue=None)
        for lexem_type, lexem in vocabulary.items():
            identificators_table[lexem_type] = {}
            d = identificators_table[lexem_type]
            for idt, word in zip_voc(vocabulary[lexem_type]):
                d[''.join(idt)] = word
        return identificators_table, identificator_size

    @staticmethod
    def prettify_struct(structure):
        """return string that contain a pretty printing of structure"""
        print('SOURCE:', structure)
        object_code = ""
        stack = []
        push = lambda x: stack.append(x)
        pop  = lambda  : stack.pop()
        last = lambda  : stack[-1] if len(stack) > 0 else ' '
        def indented_code(s, level):
            return '\t'*level + s + '\n'

        level = 0
        CONDITIONS = LEXEM_TYPE_PREDICAT + LEXEM_TYPE_CONDITION
        ACTION = LEXEM_TYPE_ACTION
        DOWNLEVEL = LEXEM_TYPE_DOWNLEVEL
        for lexem in structure:
            if lexem is ACTION:
                if last() in CONDITIONS:
                    object_code += indented_code('if ' + ' and '.join(stack) + ':', level)
                    stack = []
                    level += 1
                object_code += indented_code(lexem, level)
            elif lexem in CONDITIONS:
                push(lexem)
            elif lexem is DOWNLEVEL:
                level = max(level-1, 0)
        return object_code


# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    alphabet = '01'
    vocabulary_struct = [
        LEXEM_TYPE_CONDITION,
        LEXEM_TYPE_ACTION,
        LEXEM_TYPE_PREDICAT,
        LEXEM_TYPE_DOWNLEVEL,
    ]
    vocabulary_values = {
        LEXEM_TYPE_COMPARISON: ('temperature',),
        LEXEM_TYPE_PREDICAT  : ('haveNeighbors',),
        LEXEM_TYPE_ACTION    : ('die', 'duplicate'),
        LEXEM_TYPE_OPERATOR  : ('>', '==', '<'),
    }

    dc = DNACompiler(alphabet, vocabulary_struct, vocabulary_values)
    print(dc.compile('111010001010010110101110110110'))







