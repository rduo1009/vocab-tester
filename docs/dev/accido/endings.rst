##############
 Word classes
##############

The ``accido`` package contains classes that represent Latin words and
determine their endings. These classes are contained under ``accido.endings``.

All of these functions have the following methods:

-  ``get()`` - returns the ending of a word given the components of the ending.
-  ``find()`` - returns the possible ending components given the ending.
-  ``_create_components()`` - return the components from the dict key

They also have the following attributes:

-  ``meaning`` - the meaning of the word. Can either be a string or a
   ``MultipleMeanings``.
-  ``endings`` - the endings of the word. The keys are encoded versions of the
   ending components. The values are the endings themselves.
-  ``_first`` - the first part of the word. Used for sorting.

----

.. contents:: Table of Contents
   :backlinks: none

----

   Note: throughout these docs, if a parameter shown in the examples is used as
   a keyword argument, that means it is a keyword-only argument.

************
 Adjectives
************

There are two groups of adjectives - adjectives that take first and second
declension endings and adjectives that take third declension endings. The third
declension adjectives also come in three terminations (groups).

Creating an Adjective class
===========================

First and second declension adjectives
--------------------------------------

For the principal parts, give the nominative singular in the masculine,
feminine and neuter forms. For example:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Case, Degree, Gender, Number
   >>> adjective = Adjective(
   ...     "iratus", "irata", "iratum", declension="212", meaning="angry"
   ... )
   >>> adjective.get(
   ...     degree=Degree.POSITIVE,
   ...     gender=Gender.FEMININE,
   ...     case=Case.ACCUSATIVE,
   ...     number=Number.PLURAL,
   ... )
   'iratas'

Third declension adjectives
---------------------------

Internally, the declension of these adjectives are represented as ``3-1``,
``3-2`` and ``3-3`` for the three terminations.

One termination
^^^^^^^^^^^^^^^

For the principal parts, give the nominative singular in the masculine (which
is the same for all genders) and the genitive singular. For example:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Case, Degree, Gender, Number
   >>> adjective = Adjective(
   ...     "egens", "egentis", declension="3", termination=1, meaning="needy"
   ... )
   >>> adjective.get(
   ...     degree=Degree.POSITIVE,
   ...     gender=Gender.NEUTER,
   ...     case=Case.ACCUSATIVE,
   ...     number=Number.PLURAL,
   ... )
   'egentia'

Two termination
^^^^^^^^^^^^^^^

For the principal parts, give the masculine/feminine nominative singular and
the neuter masculine singular. For example:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Case, Degree, Gender, Number
   >>> adjective = Adjective(
   ...     "levis", "leve", declension="3", termination=2, meaning="light"
   ... )
   >>> adjective.get(
   ...     degree=Degree.POSITIVE,
   ...     gender=Gender.NEUTER,
   ...     case=Case.ACCUSATIVE,
   ...     number=Number.SINGULAR,
   ... )
   'leve'

Three termination
^^^^^^^^^^^^^^^^^

For the principal parts, give the nominative singular in the masculine,
feminine and neuter forms. For example:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Case, Degree, Gender, Number
   >>> adjective = Adjective(
   ...     "acer", "acris", "acre", declension="3", termination=3, meaning="keen"
   ... )
   >>> adjective.get(
   ...     degree=Degree.POSITIVE,
   ...     gender=Gender.FEMININE,
   ...     case=Case.DATIVE,
   ...     number=Number.PLURAL,
   ... )
   'acribus'

Adverbs
=======

The ``endings`` of adjectives also include adverb forms. For example:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Degree
   >>> adjective = Adjective(
   ...     "prudens", "prudentis", declension="3", termination=1, meaning="wise"
   ... )

   # Set adverb to True to get the adverb form.
   >>> adjective.get(degree=Degree.COMPARATIVE, adverb=True)
   'prudentius'

Irregular adjectives
====================

   Note: the irregular adjectives are hard-coded in an non-exhaustive list. Any
   contributions to this (in ``edge_cases.py``) are welcome.

Some irregular adjectives are also supported. ``accido`` supports irregular
comparative, superlative and adverb forms, and adjective that do not have an
adverb form at all.

For example with irregular forms:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Case, Degree, Gender, Number
   >>> adjective = Adjective(
   ...     "bonus", "bona", "bonum", declension="212", meaning="good"
   ... )
   >>> adjective.get(
   ...     degree=Degree.COMPARATIVE,
   ...     gender=Gender.MASCULINE,
   ...     case=Case.ACCUSATIVE,
   ...     number=Number.SINGULAR,
   ... )
   'meliorem'

   >>> adjective.get(
   ...     degree=Degree.SUPERLATIVE,
   ...     gender=Gender.MASCULINE,
   ...     case=Case.ACCUSATIVE,
   ...     number=Number.SINGULAR,
   ... )
   'optimum'

   >>> adjective.get(degree=Degree.POSITIVE, adverb=True)
   'bene'

and with no adverb form:

.. code:: python

   >>> from python_src.accido.endings import Adjective
   >>> from python_src.accido.misc import Degree
   >>> adjective = Adjective(
   ...     "dexter", "dextra", "dextrum", declension="212", meaning="skillful"
   ... )
   >>> adjective.get(
   ...     degree=Degree.POSITIVE,
   ...     adverb=True,
   ... ) # None

*******
 Nouns
*******

Nouns come in five declensions, and three genders. The declension can be
inferred from the genitive endings, but the gender of the noun must be given.
*Plurale tantum* nouns (which exists only in the plural form) are also
supported (example below). For example:

Creating a Noun class
=====================

.. code:: python

   >>> from python_src.accido.endings import Noun
   >>> from python_src.accido.misc import Case, Gender, Number
   >>> noun = Noun(
   ...     "porta", # servus, canis, manus, res
   ...     "portae", # servi, canis, manus, rei
   ...     gender=Gender.FEMININE,
   ...     meaning="gate" # slave, dog, hand, thing
   ... )
   >>> noun.get(case=Case.NOMINATIVE, number=Number.PLURAL)
   'portae'

Plurale tantum
==============

.. code:: python

   >>> from python_src.accido.endings import Noun
   >>> from python_src.accido.misc import Case, Gender, Number
   >>> noun = Noun(
   ...     "arma",
   ...     "armorum",
   ...     gender=Gender.NEUTER,
   ...     meaning="arms"
   ... )
   >>> noun.get(case=Case.GENITIVE, number=Number.PLURAL)
   'armorum'
   >>> noun.get(case=Case.NOMINATIVE, number=Number.SINGULAR) # None

Irregular nouns
===============

   Note: the irregular nouns are hard-coded in an non-exhaustive list. Any
   contributions to this (in ``edge_cases.py``) are welcome.

``accido`` groups pronouns into two groups: pronouns that have a gender (e.g.
qui), and pronouns that do not (e.g. ego). The latter group are internally
considered to be irregular nouns.

The downside of this is that 'irregular noun' pronouns cannot have a person
(i.e. 1st, 2nd, 3rd person). This means that, for example, 'ego' and 'tu' are
considered to be different.

.. code:: python

   >>> from python_src.accido.endings import Noun
   >>> from python_src.accido.misc import Case, Gender, Number
   >>> noun = Noun(
   ...     "ego",
   ...     meaning="I"
   ... )
   >>> noun.get(case=Case.DATIVE, number=Number.PLURAL)
   'nobis'

**********
 Pronouns
**********

   Note: The pronouns are hard-coded in an non-exhaustive list. Any
   contributions to this (in ``edge_cases.py``) are welcome.

The other group of pronouns (pronouns that have a gender) can be represented
using a ``Pronoun`` class.

For example:

.. code:: python

   >>> from python_src.accido.endings import Pronoun
   >>> from python_src.accido.misc import Case, Gender, Number
   >>> pronoun = Pronoun(
   ...     "qui",
   ...     meaning="who"
   ... )
   >>> pronoun.get(
   ...     case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.FEMININE
   ... )
   'quae'

***************
 Regular words
***************

Some words don't have any endings (e.g. prepositions), and so are represented
by a ``RegularWord`` class. For example:

.. code:: python

   >>> from python_src.accido.endings import RegularWord
   >>> word = RegularWord(
   ...     "et",
   ...     meaning="and",
   ... )
   >>> word.get()
   'et'

*******
 Verbs
*******

Verbs, and their participle forms are supported. Note that ``accido`` uses the
perfect passive participle form as the fourth principal part (following the
Cambridge Latin Course), not the supine as usually occurs (this might come in
the future). One can also not include the perfect passive participle form
(internally called ``ppp``), which would cause the resulting ``Verb`` object to
not have participle endings.

Creating a Verb class
=====================

Only the principal parts and the meaning need to be specified, the conjugation
can be inferred from the principal parts.

For example:

.. code:: python

   >>> from python_src.accido.endings import Verb
   >>> from python_src.accido.misc import Mood, Number, Tense, Voice
   >>> verb = Verb(
   ...     "amo",
   ...     "amare",
   ...     "amavi",
   ...     "amatus",
   ...     meaning="love",
   ... )
   >>> verb.get(
   ...     tense=Tense.IMPERFECT,
   ...     voice=Voice.ACTIVE,
   ...     mood=Mood.INDICATIVE,
   ...     number=Number.PLURAL,
   ...     person=2,
   ... )
   'amabatis'

Third declension -io verbs
--------------------------

   Note: the verbs that fall in this category are hard-coded in an
   non-exhaustive list. Any contributions to this (in ``edge_cases.py``) are
   welcome.

``accido`` supports some third declension -io verbs. For example:

.. code:: python

   >>> from python_src.accido.endings import Verb
   >>> from python_src.accido.misc import Mood, Number, Tense, Voice
   >>> verb = Verb(
   ...     "capio",
   ...     "capere",
   ...     "capivi",
   ...     "captus",
   ...     meaning="take",
   ... )
   >>> verb.get(
   ...     tense=Tense.PRESENT,
   ...     voice=Voice.ACTIVE,
   ...     mood=Mood.INDICATIVE,
   ...     number=Number.PLURAL,
   ...     person=3,
   ... )
   'capiunt'

Participle forms
================

Participles are also supported. When getting a participle form using ``get()``,
set the mood to ``Mood.PARTICIPLE``. (Only the perfect passive participle form
and the present active participle are supported at the moment).

For example:

.. code:: python

   >>> from python_src.accido.endings import Verb
   >>> from python_src.accido.misc import Case, Gender, Mood, Number, Tense, Voice
   >>> verb = Verb(
   ...     "amo",
   ...     "amare",
   ...     "amavi",
   ...     "amatus",
   ...     meaning="love",
   ... )
   >>> verb.get(
   ...     tense=Tense.PERFECT,
   ...     voice=Voice.PASSIVE,
   ...     mood=Mood.PARTICIPLE,
   ...     participle_case=Case.ACCUSATIVE,
   ...     number=Number.PLURAL,
   ...     participle_gender=Gender.FEMININE,
   ... )
   'amatas'

No participle forms
-------------------

Not including the perfect passive participle form in the ``Verb`` object will
mean that there will be not participle endings.

.. code:: python

   >>> from python_src.accido.endings import Verb
   >>> from python_src.accido.misc import Case, Gender, Mood, Number, Tense, Voice
   >>> verb = Verb(
   ...     "amo",
   ...     "amare",
   ...     "amavi",
   ...     meaning="love",
   ... )
   >>> verb.get(
   ...     tense=Tense.PERFECT,
   ...     voice=Voice.PASSIVE,
   ...     mood=Mood.PARTICIPLE,
   ...     participle_case=Case.ACCUSATIVE,
   ...     number=Number.PLURAL,
   ...     participle_gender=Gender.FEMININE,
   ... ) # None

Irregular verbs
===============

   Note: the irregular verbs are hard-coded in an non-exhaustive list. Any
   contributions to this (in ``edge_cases.py``) are welcome.

Some irregular verbs are also supported by ``accido``.

.. code:: python

   >>> from python_src.accido.endings import Verb
   >>> from python_src.accido.misc import Mood, Number, Tense, Voice
   >>> verb = Verb(
   ...     "fero",
   ...     "ferre",
   ...     "tuli",
   ...     "latus",
   ...     meaning="carry",
   ... )
   >>> verb.get(
   ...     tense=Tense.PRESENT,
   ...     voice=Voice.ACTIVE,
   ...     mood=Mood.INDICATIVE,
   ...     number=Number.PLURAL,
   ...     person=3,
   ... )
   'ferunt'
