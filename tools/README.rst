
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



jsonformatter.py
------------------------------------------------------------------------

(Re-)indent json on stdin and send it to stdout.

Handy for webservices that return json as one big long string. With ``curl
http://the.json.url/ | jsonformatter`` you can actually read it.




(See `source code on github <https://github.com/reinout/tools/blob/master/tools/jsonformatter.py>`_).



mkinit.py
------------------------------------------------------------------------


Create a directory and pre-fill it with an ``__init__.py``

Basically: mkdir plus the creation of the init file. Handy for creating a
django app's ``$APP/management/commands/`` directory.


(See `source code on github <https://github.com/reinout/tools/blob/master/tools/mkinit.py>`_).



naw.py
------------------------------------------------------------------------


Company-internal script to query our telephone list.

We have an internal tool that regularly pings laptops to see if somebody's in
the house. That data, combined with a telephone number list, is available as a
JSON file.

This script reads the json and prints it, optionally filtered with

(Script is from Arjan Verkerk, not me, btw. Though I modified it a bit to run
as a setuptools console script.)



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/naw.py>`_).



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



timelog.py
------------------------------------------------------------------------


This is a gtimelog variant/hack for the commandline.

`gtimelog <http://mg.pov.lt/gtimelog/>`_ requires gtk, which isn't handy on
OSX. Years ago I already hacked up a modified version that only requires the
commandline. I've dug it up again.

gtimelog is (c) Marius Gedminas, GPL. My stuff is GPL'ed too, so that fits :-)

My variant works on the commandline and provides two commands:

tl
    Add a timelog entry to the logfile. The entry to add is passed on the
    commandline, for instance ``tl weblog`` for when I worked on a blog
    entry.

    The logfile is ``~/.gtimelog/timelog.txt``.

pt
    Short for "print today", it prints an overview of how much time I spend on
    what today. Call it like ``pt week`` to get an overview of the whole week
    (and a couple of earlier weeks, in case I need that).

The ``tl`` command works best when you add tab completion. Add a
``~/.gtimelog/tasks.txt`` file, which should have one word per line, each
being a task you want to log with ``tl``. Hook up the following into your bash completion::

    _timelog()
    {
        local cur prev
        COMMAND_NAME='timelog'
        COMPREPLY=()
        # Word that is currently being expanded:
        cur=${COMP_WORDS[COMP_CWORD]}
        # Previous expanded word:
        prev=${COMP_WORDS[COMP_CWORD-1]}

        # We look for ~/.gtimelog/tasks.txt, which should have one word
        # per line, each being a project.
        CONFIGDIR=~/.gtimelog
        if test ! -d $CONFIGDIR; then
            return 0
        fi
        PROJECTS="$(cat $CONFIGDIR/tasks.txt | grep -v \#)"
        COMPREPLY=( $(compgen -W '$PROJECTS' -- $cur ) )
    }
    complete -F _timelog tl

Works quite well!



(See `source code on github <https://github.com/reinout/tools/blob/master/tools/timelog.py>`_).



vagrant.py
------------------------------------------------------------------------


Script to run a command via ssh inside vagrant.

What it does: we're inside a directory that we know has been mounted in a
local vagrant box. We ``cd`` to the corresponding directory and run the
command there.

There are quite some assumptions in here, they match the way I (Reinout) has
set it all up:

- Virtual machines are inside ``~/vm/VM_NAME/``.

- That ``~/vm/VM_NAME/`` directory is mounted as ``/vagrant/`` inside the VM.

- The vm name is "django" for a vm inside ~/vm/django/`` and it has a
  corresponding alias inside your ssh config file. So ssh'ing to "django"
  means you connect just fine to the right VM with the vagrant user. An
  example of such a config that ought to go inside ``~/.ssh/config`` ::

     Host django
         HostName 33.33.33.20
         User vagrant

  Oh, and make sure you use ``ssh-copy-id`` to copy your ssh key to the
  vagrant box, otherwise you'll go mad typing your password all the time.




(See `source code on github <https://github.com/reinout/tools/blob/master/tools/vagrant.py>`_).

