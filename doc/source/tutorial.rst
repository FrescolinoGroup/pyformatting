Tutorial
========

Shortening strings
------------------

Strings can be shortened to a given maximum length using the :func:`.shorten` function. 

.. code :: python

    >>> import fsc.formatting
    >>>
    >>> long_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    >>> fsc.formatting.shorten(long_string)
    'Lorem ipsum dolor s<...406...>anim id est laborum.'
    
The ``length`` keyword can be used to change how long the final string will be.
    
.. code :: python

    >>> fsc.formatting.shorten(long_string, length=20)
    'Lore<...436...>orum.'
    
Finally, the ``show_number`` keyword can be used to show or hide the number indicating by how much the string has been cut.

.. code :: python

    >>> fsc.formatting.shorten(long_string, length=20, show_number=False)
    'Lorem i<...>laborum.'

Drawing a box around a string
-----------------------------

The :func:`.to_box` function can be used to draw a box around a paragraph. 

.. code :: python

    >>> import fsc.formatting
    >>> print(fsc.formatting.to_box('line 1\nline 2'))
    +----------------------------------------------------------------------+
    |                                line 1                                |
    |                                line 2                                |
    +----------------------------------------------------------------------+

The width of the box must be at least as wide as the longest line in the string, otherwise the box will appear broken.
    
.. code :: python 

    >>> print(fsc.formatting.to_box('line 1\nline 2 is way too long, it is longer than the width of the box! this will look quite ugly!'))
    +----------------------------------------------------------------------+
    |line 1                                                                |
    |line 2 is way too long, it is longer than the width of the box! this will look quite ugly!|
    +----------------------------------------------------------------------+

The ``padding`` keyword can be used to manually align the strings on the left side. The ``width`` keyword gives the (inner) width of the box.

.. code :: python

    >>> print(fsc.formatting.to_box('line 1\nline 2', padding=3, width=20))
    +--------------------+
    |   line 1           |
    |   line 2           |
    +--------------------+
    
Finally, the ``centering_line`` keyword can be used to determine whether the first or longest line is centered. This only works if the padding is not set explicitly.

.. code :: python
    
    >>> print(fsc.formatting.to_box('line 1\nline 2 is longer', width=30))
    +------------------------------+
    |       line 1                 |
    |       line 2 is longer       |
    +------------------------------+
    >>> print(fsc.formatting.to_box('line 1\nline 2 is longer', width=30, centering_line='first'))
    +------------------------------+
    |            line 1            |
    |            line 2 is longer  |
    +------------------------------+

    
