# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
Spell function
Modified by Subrata Sarkar
https://github.com/SubrataSarkar32
Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
from autocorrect.nlp_parser import NLP_COUNTS
from autocorrect.nlp_parser_bn import NLP_COUNTS as NLP_COUNTS_BN
from autocorrect.word import Word, common, exact, known, get_case

def spell(word,language='en'):
    """The language parameter takes into account of the language.
       most likely correction for everything up to a double typo"""
    if(language == 'en'):
        w = Word(word)
        candidates = (common([word]) or exact([word]) or known([word]) or
                      known(w.typos()) or common(w.double_typos()) or
                      [word])
        correction = max(candidates, key=NLP_COUNTS.get)
        return get_case(word, correction)
    elif(language == 'bn'):
        w = Word(word)
        candidates = (common([word]) or exact([word]) or known([word]) or
                      known(w.typos()) or common(w.double_typos()) or
                      [word])
        correction = max(candidates, key=NLP_COUNTS_BN.get)
        return get_case(word, correction)
    else:
        raise ValueError("This language is not supported")
