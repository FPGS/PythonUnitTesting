# -*- coding: utf-8 -*-
from Christmas import FunWithSnow

clase = FunWithSnow()


def test_IsPalindrome():
    assert (clase.isPalindrome("A Mercedes ése de crema"))
    assert (clase.isPalindrome("Ana, la tacaña catalana"))
    assert not (clase.isPalindrome("dado"))
    assert not (clase.isPalindrome("ddia"))

def test_ReverseWordsOnAString():
    assert (clase.reverseString("esta casa es un ruina")== "atse asac se nu aniur")

def test_ReverseWordsOnAList():
    assert (clase.reverseList(['esta', 'casa', 'es', 'un', 'ruina'])== "atse asac se nu aniur")



