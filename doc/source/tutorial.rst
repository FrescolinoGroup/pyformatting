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
