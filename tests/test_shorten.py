#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.08.2016 00:10:14 CEST
# File:    test_shorten.py

import pytest
import fsc.formatting

LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

def test_shorten_base():
    assert fsc.formatting.shorten(LOREM_IPSUM) == 'Lorem ipsum dolor s<...406...>anim id est laborum.'
    
def test_shorten_length():
    assert fsc.formatting.shorten(LOREM_IPSUM, length=20) == 'Lore<...436...>orum.'

def test_shorten_number():
    assert fsc.formatting.shorten(LOREM_IPSUM, length=20, show_number=False) == 'Lorem i<...>laborum.'
