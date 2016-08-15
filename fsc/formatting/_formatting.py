#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>, Dominik Gresch <greschd@gmx.ch>
# Date:    11.04.2016 09:54:50 CEST
# File:    _formatting.py

from __future__ import division, print_function

import re
import math
import warnings
import collections as co
try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch # Python 3.3 and lower

from fsc.export import export

@export
def shorten(obj, length=50, show_number=True):
    """
    Returns the str representation of an object and shortens it if longer than ``length``.
    
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

@export
def without_ansi(string):
    """Removes ANSI escape codes which match one of the two patterns '\x1b[^m]*m' and '\x1b\([A-Z]' from the string."""
    ansi_escape = re.compile(r'\x1b[^m]*m', re.IGNORECASE)
    string = ansi_escape.sub('', string)
    pattern = re.compile(r'\x1b\([A-Z]', re.IGNORECASE)
    return pattern.sub('', string)

@export
@singledispatch
def to_box(
    iterable,
    width=70,
    padding='auto',
    centering_line='longest'
):
    """
    Returns a string where a box is drawn around the given string (or iterable of strings). The length of each line should not be longer than the width of the box, otherwise the box might look bad.
    
    :param width:   Width of the box, without the box itself.
    :type width:    int
    
    :param padding: Space on the left side of the string. Per default (``padding='auto'``), the padding is such that the ``centering_line`` is centered. 
    :type padding:  int

    :param centering_line:  Determines which line should be centered. Valid arguments are 'first' and 'longest'. 
    :type centering_line:   str
    """
    padding = min([_box_padding(string, centering_line, width) for string in iterable])
    output = ''
    for string in iterable[:-1]:
        output += to_box(
            string,
            padding=padding,
            width=width,
            centering_line=centering_line,
            no_endline = True
        )
    output += to_box(
        iterable[-1],
        padding=padding,
        width=width,
        centering_line=centering_line,
        no_endline = False
    )
    return output

@to_box.register(str)
def _(
    string,
    width=70,
    padding="auto",
    centering_line="longest",
    no_endline=False
):
    # splitting the string into lines
    lines = string.split('\n')

    # getting the values for padding
    if(padding == "auto"):
        padding = _box_padding(string, centering_line, width)

    # checking total size
    for line in lines:
        if(len(without_ansi(line)) > width - padding):
            warnings.warn("strings too long, might look ugly",
            UserWarning)

    # creating the string
    endline = '+' + width * '-' + '+'
    box_str = endline + '\n'

    for line in lines:
        line_temp = '|' + padding * ' ' + line
        line_temp += ' ' * max(0, (width + 1 - len(without_ansi(line_temp)))) + '|\n'
        box_str += line_temp
    if not no_endline:
        box_str += endline
    return box_str

def _box_padding(string, centering_line, width):
    lines = string.split('\n')
    if(centering_line != "first" and centering_line != "longest"):
        warnings.warn("centering_line: invalid argument, using 'longest'",
        UserWarning)
    if centering_line == 'first':
        text_width = len(without_ansi(lines[0]))
    elif centering_line == 'longest': # longest
        text_width = max([len(without_ansi(line)) for line in lines])
    else:
        raise ValueError("Unknown value '{}' for 'centering_line', must be one of {{'first', 'longest'}}".format(centering_line))
    return (width - text_width) // 2
