#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.08.2016 00:14:43 CEST
# File:    test_tobox.py

import pytest
import fsc.formatting

def test_box():
    assert fsc.formatting.to_box('line 1\nline 2') == '+----------------------------------------------------------------------+\n|                                line 1                                |\n|                                line 2                                |\n+----------------------------------------------------------------------+'

def test_box_width():
    assert fsc.formatting.to_box('line 1\nline 2', width=20) == '+--------------------+\n|       line 1       |\n|       line 2       |\n+--------------------+'
    
def test_box_padding():
    assert fsc.formatting.to_box('line 1\nline 2', width=20, padding=2) == '+--------------------+\n|  line 1            |\n|  line 2            |\n+--------------------+'
    
def test_box_centering():
    fsc.formatting.to_box('line 1\nlonger line 2', width=20, centering_line='first') == '+--------------------+\n|       line 1       |\n|       longer line 2|\n+--------------------+'
