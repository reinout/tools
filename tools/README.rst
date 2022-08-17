
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


dtname.py
------------------------------------------------------------------------


Helper script to generate a zettelkasten ID (YYYYMMDDHHMM-some-info.md) filename

dtname by itself just outputs ``202208171545.md``, ``dtname some info`` gives
you ``202208171545-some-info.md``



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/dtname.py>`_).


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


git.py
------------------------------------------------------------------------


Add/commit/push a git checkout in one command ("gac", for "Git Add Commit").

Lots of my personal stuff is in git, so I need to do a lot of ``git add -u``,
``git commit -m "update"`` and ``git push``. Note the ``"update"``
message. I'm often not bothering with more descriptive commit messages.

The script *does* ask for confirmation after first showing the status:
prevent accidents.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/git.py>`_).


github.py
------------------------------------------------------------------------


Open github page for your current directory in your browser.

You're working on the commandline and want to check something for the github
project you're working on. This script (called ``gh``) looks up the github url
for your project and opens it in your webbrowser.

If you call it like ``gh issues``, you'll get the issues page.

I got the idea from https://github.com/myusuf3/octogit.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/github.py>`_).


mkinit.py
------------------------------------------------------------------------


Create a directory and pre-fill it with an ``__init__.py``

Basically: mkdir plus the creation of the init file. Handy for creating a
django app's ``$APP/management/commands/`` directory.


(See `source code on github <https://github.com/reinout/tools/blob/master/tools/mkinit.py>`_).


python_coding_cleanup.py
------------------------------------------------------------------------

Zap 'coding: utf-8' header from python files in the current directory.

The header isn't needed anymore in python 3, so for most projects, it can be
removed.



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/python_coding_cleanup.py>`_).


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
