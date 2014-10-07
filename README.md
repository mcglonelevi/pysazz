Pysazz
======

Pysazz - a CLI written in Python designed to manage SASS-based CSS Frameworks

##Installation

Set up a variable in your path for the executable: pysazz.py, or you can run it locally using Python 3.4.1 by running "python pysazz.py"

##Commands

At the moment Pysazz has 3 commands:

pysazz init - creates the basic config file

pysazz compile [-arg] - downloads files and compiles, arguments are optional, but the include "-compressed", "-compact", "-expanded".  "-nested" is the default argument.

pysazz update - redownloads all files and overwrites them.  Be careful when using as any changes made to downloaded files will be overwritten.

##Dependencies.

Please have libsass installed before use.
https://pypi.python.org/pypi/libsass

##XML Formatting

Take a look at the included config file.  Basically, you specify a folder attribute and a url inside of a link tag.

##Documentation

Look here for a more detailed explanation of how to use Pysazz: http://mcglonelevi.github.io/pysazz/
