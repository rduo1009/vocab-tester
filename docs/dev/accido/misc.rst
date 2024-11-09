#########################
 Miscellaneous utilities
#########################

The ``accido`` package also has additional utilities for working with Latin
words, contained under ``accido.misc``.

*******
 Enums
*******

Various enums are used throughout the ``accido`` package to represent the
components of Latin endings (e.g. case, grammatical number). They have two
attributes:

-  ``regular`` - the regular form of the enum
-  ``shorthand`` - the shorthand form of the enum, used in the keys of the
   ending dictionaries (e.g. 'nominative' -> 'nom')

For example:

.. code:: python

   >>> from python_src.accido.misc import Case
   >>> Case.NOMINATIVE.regular
   'nominative'
   >>> Case.NOMINATIVE.shorthand
   'nom'

******************
 EndingComponents
******************

Represent the ending components of a Latin ending. In ``accido`` functions, the
ending components are often given as the parameters of the functions, but
outside of ``accido``, the ending components are packaged into a
``EndingComponents`` object.

Examples can be seen in the ``EndingComponents`` docstring.

******************
 MultipleMeanings
******************

Represents multiple meanings of a word. The first meaning is the primary
meaning, the other meanings are secondary meanings.

For example:

.. code:: python

   MultipleMeanings(("happy", "joyous", "glad"))

*****************
 MultipleEndings
*****************

Represents multiple endings of a ending components. There is usually a
``regular`` ending, and then the other endings are given with a keyword that
describes their usage.

For example, some endings are used for regular genitives, while others are used
for partitive genitives, which would look like this:

.. code:: python

   MultipleEndings(regular="vestri", partitive="vestrum")
