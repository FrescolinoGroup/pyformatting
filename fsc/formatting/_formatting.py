#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2016 09:54:50 CEST
# File:    _formatting.py

from __future__ import division, print_function

__all__ = ["sstr"]

import math

def sstr(obj, length = 50):
    """
    Returns the str representation of an object, and shortens it, if it is too long.
    
    Args:
        obj:  Any python object that we want to convert to a string.
        length (int): The maximal length of the resulting string.
    
    Returns:
        str.  This string is guaranteed to have maximal size length.

    """
    output = str(obj)
    if len(output) > length: # shorten too long objects to certain size
        not_shown = len(output) - length + 8
        nslen = len(str(not_shown))
        not_shown += nslen
        if len(str(not_shown)) > nslen:
            not_shown += 1
        
        half_shown = (len(output) - not_shown)/2
        
        output = output[:math.floor(half_shown)] + " ...{}... ".format(not_shown) + output[-math.ceil(half_shown):]
    return output

