Pysazz
======

Pysazz - a CLI written in Python designed to manage SASS-based CSS Frameworks

Installation

Set up a variable in your path for the executable: pysazz.py, or you can run it locally using Python 3.4.1 by running "python pysazz.py"

Commands

At the moment Pysazz has 2 commands:

pysazz init - creates the basic config file

pysazz compile [-arg] - downloads files and compiles, arguments are optional, but the include "-compressed", "-compact", "-expanded".  "-nested" is the default argument.

Dependencies.

Please have libsass installed before use.
https://pypi.python.org/pypi/libsass

XML Formatting

Take a look at the included config file.  Basically, you specify a folder attribute and a url inside of a link tag.
