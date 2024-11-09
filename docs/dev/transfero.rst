######################################
 transfero - inflecting English words
######################################

The ``transfero`` package allows ``vocab-tester`` to find the inflections of
English words, based on the grammatical components of the Latin endings. The
features of this package are all in the ``transfero.words.find_inflection``
function. The ``find_inflection`` function takes three parameters:

-  ``word`` - the word to inflect (string)
-  ``components`` - the ending components of the inflection (EndingComponents)
-  ``main`` - whether to return the main inflection (True) or all possible
      inflections (False)

Note that the ``main`` parameter defaults to False.

**********
 Examples
**********

   For more exhaustive examples, see the tests for transfero.

.. code:: python

   >>> from python_src.transfero.words import find_inflection
   >>> from python_src.accido.misc import (
   ...     Case,
   ...     Degree,
   ...     EndingComponents,
   ...     Gender,
   ...     Mood,
   ...     Number,
   ...     Tense,
   ...     Voice,
   ... )

   >>> find_inflection("into", EndingComponents(string=""))
   {'into'}
   >>> find_inflection("into", EndingComponents(string=""), main=True)
   'into'

   >>> find_inflection(
   ...     "this",
   ...     EndingComponents(
   ...         case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE
   ...     ),
   ... )  # doctest: +SKIP
   {'for these', 'to these'}
   >>> find_inflection(
   ...     "this",
   ...     EndingComponents(
   ...         case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE
   ...     ),
   ...     main=True,
   ... )
   'for these'

   >>> find_inflection(
   ...     "happy",
   ...     EndingComponents(
   ...         case=Case.NOMINATIVE,
   ...         gender=Gender.MASCULINE,
   ...         number=Number.SINGULAR,
   ...         degree=Degree.COMPARATIVE,
   ...     ),
   ... )  # doctest: +SKIP
   {'happier', 'more happy'}
   >>> find_inflection(
   ...     "happy",
   ...     EndingComponents(
   ...         case=Case.NOMINATIVE,
   ...         gender=Gender.MASCULINE,
   ...         number=Number.SINGULAR,
   ...         degree=Degree.COMPARATIVE,
   ...     ),
   ...     main=True,
   ... )
   'happier'

   >>> find_inflection(
   ...     "sad",
   ...     EndingComponents(degree=Degree.SUPERLATIVE),
   ... ) # doctest: +SKIP
   {'too sadly', 'very sadly', 'extremely sadly', 'quite sadly', 'most sadly', 'rather sadly'}
   >>> find_inflection(
   ...     "sad",
   ...     EndingComponents(degree=Degree.SUPERLATIVE),
   ...     main=True,
   ... )
   'most sadly'

   >>> find_inflection(
   ...     "man",
   ...     EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR),
   ... ) # doctest: +SKIP
   {'of the man', 'of a man', "man's"}
   >>> find_inflection(
   ...     "man",
   ...     EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR),
   ...     main=True,
   ... )
   'of the man'

   >>> find_inflection(
   ...     "run",
   ...     EndingComponents(
   ...         tense=Tense.PRESENT,
   ...         voice=Voice.ACTIVE,
   ...         mood=Mood.INFINITIVE,
   ...     )
   ... )
   {'to run'}
   >>> find_inflection(
   ...     "run",
   ...     EndingComponents(
   ...         tense=Tense.PRESENT,
   ...         voice=Voice.ACTIVE,
   ...         mood=Mood.INFINITIVE,
   ...     ),
   ...     main=True,
   ... )
   'to run'

   >>> find_inflection(
   ...     "attack",
   ...     EndingComponents(
   ...         tense=Tense.PERFECT,
   ...         voice=Voice.PASSIVE,
   ...         mood=Mood.PARTICIPLE,
   ...         gender=Gender.MASCULINE,
   ...         number=Number.PLURAL,
   ...         case=Case.ACCUSATIVE
   ...     )
   ... )
   {'having been attacked'}
   >>> find_inflection(
   ...     "attack",
   ...     EndingComponents(
   ...         tense=Tense.PERFECT,
   ...         voice=Voice.PASSIVE,
   ...         mood=Mood.PARTICIPLE,
   ...         gender=Gender.MASCULINE,
   ...         number=Number.PLURAL,
   ...         case=Case.ACCUSATIVE
   ...     ),
   ...     main=True,
   ... )
   'having been attacked'
