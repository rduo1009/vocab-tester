####################################
 Dev documentation for vocab-tester
####################################

This is the development documentation for the core of vocab-tester. It is
intended for anyone wanting to contribute to the project, or for anyone
interested about the inner workings of vocab-tester.

Notes about the accido package (Latin word endings) are in the *accido* folder.
Notes about the transfero package (inflecting English words) are in
*transfero.rst*.

***************
 General notes
***************

-  Running mypy on this is very important. I removed some input validation in
   favour of using type hints and enums instead. However, this means code like
   this will run:

.. code:: python

   foo = Adjective("egens", "egentis", termination=100, declension="100", meaning="poor")

Mypy would spot the issues, but this code will run without errors.

-  Some code in this project (especially ``rogo.asker``) is a complete mess. I
   will have to fix things up at some point.
-  The type stubs provided by this project are not complete, rather they exist
   to help with type hinting and keep mypy happy.
