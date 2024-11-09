####################################
 accido - determining Latin endings
####################################

The ``accido`` package allows ``vocab-tester`` to find the endings of Latin
words. It also provides various utilities for working with Latin words.

****************
 accido.endings
****************

The ``endings`` package provides support for:

-  adjectives (with adverb forms)
-  verbs (and participles)
-  nouns
-  pronouns
-  words with only one ending (called *regulars* internally)

For more info, see the ``endings`` package documentation.

Example
=======

For example, with nouns:

.. code:: python

   >>> from src.core.accido.endings import Noun
   >>> from src.core.accido.misc import Case, Gender, Number
   >>> noun = Noun(
   ...     "servus",
   ...     "servi",
   ...     gender=Gender.MASCULINE,
   ...     meaning="slave",
   ... )
   >>> noun.get(case=Case.GENITIVE, number=Number.PLURAL)
   'servorum'

*************
 accido.misc
*************

The ``misc`` package adds utilities for working with Latin words. For more
info, see the ``misc`` package documentation.

Example
=======

For example with a ``MultipleMeanings``:

.. code:: python

   >>> from src.core.accido.misc import MultipleMeanings
   >>> ending = MultipleMeanings(["happy", "joyful"])
   >>> str(ending)
   'happy'
