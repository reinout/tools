
Python script documentation
===========================

Note: this documentation is automatically generated from the docstrings at the
top of the Python scripts.



add_time.py
------------------------------------------------------------------------


Simple script to add the current time to a screenshot.

Pass in the filename of the screenshot as an argument and the script will
create a new file (named after the time, in the current directory) with the
time written in the lower right corner.

The location of the time string and the location of the font to use is
hardcoded.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/add_time.py>`_).



blog.py
------------------------------------------------------------------------


Helper scripts for me to manage my blog.

I write my blog entries as restructured text files. The ``copytoblog`` command
copies the text file to the correct date's blog subdirectory, creating it if
necessary.

There's also a command to open today's entries in emacs.

Note that some of this might be better placed inside my website project
instead of here. TODO.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/blog.py>`_).



engineerlog.py
------------------------------------------------------------------------


Simple script to add notes to a logfile from the command line.

The idea, that I read somewhere, is that a good engineer should keep logs of
what he does so that he can look at it later. It helps me quite a lot as I
regularly encounter a weird problem, knowing that I solved it earlier. But not
remembering what the solution was.

So either I have to write a blog entry about it so that I can find it in
google, or I need to add it to a simple text-based logfile somewhere. That's
what this script does.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/engineerlog.py>`_).



jshint.py
------------------------------------------------------------------------


Script for running the jshint.js javascript checker on a file or directory.


(See `source code on github <https://github.com/reinout/tools/blob/master/tools/jshint.py>`_).



sommen.py
------------------------------------------------------------------------


Small utility script for printing a bunch of calculations for my kids.


(See `source code on github <https://github.com/reinout/tools/blob/master/tools/sommen.py>`_).



thunderbird.py
------------------------------------------------------------------------

Fix the thunderbird newsrc settings

The settings sometimes contain lines like::

  gmane.comp.python.distutils.devel: 1-12428,12431-12446

There's a two-article 'hole' in there that shows up as two unread messages.
This script removes the holes.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/thunderbird.py>`_).

