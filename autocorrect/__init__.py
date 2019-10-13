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

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
from autocorrect.nlp_parser import NLP_COUNTS
from autocorrect.word import Word, common, exact, known, get_case
import re

special_chars = ['.', ',', '!', '?', ';', ':']
"""these are the same characters used in the function GetWords"""
def getWords(data):
    return re.findall(r"[\w']+|[.,!?;:]",data)

def spell(word):
    """most likely correction for everything up to a double typo"""
    w = Word(word)
    candidates = (common([word]) or exact([word]) or known([word]) or
                  known(w.typos()) or common(w.double_typos()) or
                  [word])
    correction = max(candidates, key=NLP_COUNTS.get)
    return get_case(word, correction)

def spell_sentence(sentence):
    """We essentially take each word out, and pass through the spell function
    And later append it into an empty stringself.
    Special characters are not passed through the spell function."""
    words = getWords(sentence)
    sentence = ''
    for word in words:
        if word in special_chars:
            sentence = sentence[:-1]
            sentence = sentence + word + ' '
        else:
            sentence = sentence + spell(word) + ' '
    return sentence
