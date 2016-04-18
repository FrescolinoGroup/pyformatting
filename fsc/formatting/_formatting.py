#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2016 09:54:50 CEST
# File:    _formatting.py

from __future__ import division, print_function

import math
import blessings

from fsc.export import export

@export
def shorten(obj, length=50, show_number=True):
    """
    Returns the str representation of an object, and shortens it, if it is too long.
    
    :param obj: Any python object that should be converted to a string.

    :param length: The maximal length of the resulting string.
    :type length: int

    :param show_number: Controls whether the number of omitted characters is shown (``<...N...>``) or not (``<...>``).
    :type show_number: bool

    Returns:
        str.  This string is guaranteed to have maximal size ``length``.

    """
    output = str(obj)
    if len(output) > length: # shorten too long objects to certain size
        if show_number:
            format_str = '<...{}...>'
        else:
            format_str = '<...>'

        not_shown = 0
        placeholder = format_str.format(not_shown)
        # check if the placeholder has grown in size and adjust accordingly
        while len(output) - not_shown + len(placeholder) > length:
            not_shown = len(output) - length + len(placeholder)
            placeholder = format_str.format(not_shown)

        # if not_shown grows larger than the original string, the formatting doesn't work
        if len(output) < not_shown:
            raise ValueError("'length={}' too small to shorten string '{}' of length {}.".format(length, output, len(output)))
        
        half_shown = (len(output) - not_shown) / 2 # must be int
        output = output[:math.floor(half_shown)] + placeholder + output[-math.ceil(half_shown):]

    return output

#~ @export
#~ def nice_class_name(obj):
    #~ output = str(obj.__class__)
    #~ output = output.split("'")[1]
    #~ #remove hidden modules (starting with _)
    
    #~ output = output.split(".")
    #~ output = (s for s in output if not s.startswith("_"))
    
    #~ return ".".join(output)

#~ @export
#~ def error_prefix(obj):
    #~ tc = blessings.Terminal()
    #~ return tc.bold_white_on_red(nice_class_name(obj) + ":") + " "
