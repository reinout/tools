
Shell script documentation
==========================

Note: this documentation is automatically generated from the comments in the
shell scripts.



bdr
------------------------------------------------------------------------

Run Django, also on the external interfaces for iPad testing.
'bdr' is a mnemonic for 'bin django runserver'.
Note that I'm mostly running django inside dockers nowadays :-)

Source code::

    #!/bin/bash

    docker-compose run --service-ports web python manage.py runserver 0.0.0.0:5000


create_git_repo.sh
------------------------------------------------------------------------

Initialize a git repository in the temp directory and push it to my own
server. I should have created a repository there on the server already with
``git init ~/repos/the_project_name --bare``.

Source code::

    #!/bin/bash

    set -e
    cd /tmp
    git init "$1"
    cd "$1"
    echo "hurray" > README.rst
    git add README.rst
    git commit -m "Added readme"
    git remote add origin "ssh://vanrees.org/~/repos/$1"
    git push origin master


dos2unix.py
------------------------------------------------------------------------


Copied from somewhere, I don't know wherefrom anymore.  What it does is
convert from ``\r\n`` to just ``\n`` in case you've got files with windows
line endings.

TODO:

- Clean up a bit, make it pep8-compliant.

- Check that it works (as I had the impression it didn't work all the time).

Source code::

    #!/usr/bin/env python3

    import getopt
    import os
    import re
    import shutil
    import sys


    def dos2unix(data):
        return "\n".join(data.split("\r\n"))


    def unix2dos(data):
        return "\r\n".join(dos2unix(data).split("\n"))


    def confirm(file_):
        s = raw_input("%s? " % file_)
        return s and s[0] == "y"


    def usage():
        print(
            """\
    USAGE
        dos2unix.py [-iuvnfcd] [-b extension] file {file}
    DESCRIPTION
        Converts files from unix to dos and reverse. It keeps the
        mode of the file.
        Binary files are not converted unless -f is specified.
    OPTIONS
        -i      interactive (ask for each file)
        -u      unix2dos (inverse functionality)
        -v      print files that are converted
        -n      show but don't execute (dry mode)
        -f      force. Even if the file is not ascii convert it.
        -b ext  use 'ext' as backup extension (default .bak)
        -c      don't make a backup
        -d      keep modification date and mode
    """
        )
        sys.exit()


    def main():
        try:
            opts, args = getopt.getopt(sys.argv[1:], "fniuvdc")
            args[0]
        except:
            usage()
        force = 0
        noaction = 0
        convert = dos2unix
        verbose = 0
        copystat = shutil.copymode
        backup = ".bak"
        nobackup = 0
        interactive = 0
        for k, v in opts:
            if k == "-f":
                force = 1
            elif k == "-n":
                noaction = 1
                verbose = 1
            elif k == "-i":
                interactive = 1
            elif k == "-u":
                convert = unix2dos
            elif k == "-v":
                verbose = 1
            elif k == "-b":
                backup = v
            elif k == "-d":
                copystat = shutil.copystat
            elif k == "-c":
                nobackup = 1
        asciiregex = re.compile("[ -~\r\n\t\f]+")
        for file_ in args:
            if not os.path.isfile(file_) or file_[-len(backup) :] == backup:
                continue
            fp = open(file_)
            head = fp.read(10000)
            if force or len(head) == asciiregex.match(head):
                data = head + fp.read()
                newdata = convert(data)
                if newdata != data:
                    if verbose and not interactive:
                        print(file_)
                    if not interactive or confirm(file_):
                        if not noaction:
                            newfile = file_ + ".@"
                            f = open(newfile, "w")
                            f.write(newdata)
                            f.close()
                            copystat(file_, newfile)
                            if backup:
                                backfile = file_ + backup
                                os.rename(file_, backfile)
                            else:
                                os.unlink(file_)
                            os.rename(newfile, file_)
                            if nobackup:
                                os.unlink(backfile)


    try:
        main()
    except KeyboardInterrupt:
        pass


duh
------------------------------------------------------------------------

Just print out the disk usage *totals* for every directory in the current
directory.

-m  = In megabytes (for easy "| sort -n")
-d1 = Current directory + one level below

Source code::

    #!/bin/bash

    du -m -d1


emacsclient-from-iterm
------------------------------------------------------------------------

Script to edit files in emacs by clicking on them in iterm

Enable it in iterm by going to the config. Look in the "profiles" section
for "advanced", there you can enable "semantic history" with a command like
this:

/Users/reinout/zelf/tools/bin/emacsclient-from-iterm \1 \2

\1 is the filename, \2 is the line number, if available.

Source code::

    #!/bin/bash
    FILENAME=$1
    LINENUMBER=$2

    exec /opt/homebrew/bin/emacsclient -n +${LINENUMBER:=1} "${FILENAME}"


es
------------------------------------------------------------------------

Shortcut for starting emacs

Note that I've got it set up in server mode. I've got a bash alias "e" that
edits a file with "emacsclient". So "es" stands for "emacs server" in my
case, "e" is for editing with emacs itself :-)

Source code::

    #!/bin/bash

    /usr/bin/emacs &


filefind
------------------------------------------------------------------------

Find filenames in the current directory.

- It greps case-insensitive for patial matches, so 'htm' finds
  ``index.HTML`` just fine.

- It ignores ``.git`` and ``.hg`` directories.

- It doesn't color code the output to help with emacs integration.

- It adds ``:1:`` so that you can use it in emacs' grep viewer. Clicking on
  it opens that file.

Source code::

    #!/bin/bash

    clear -x
    echo "Suggestion: use 'fd' instead"
    find -L . | grep --colour=never -i "$1" | grep -v '.git/' |grep -v '.hg/' |sed 's/^\.\///g'|sed 's/\(.*\)/\1:1:/g'
    # grep -i --color=auto $1


md-to-doc
------------------------------------------------------------------------

Use pandoc to convert a .md file to docx.

I originally used the `markdown` format, but I've switched to `gfm`, github
flavoured markdown, because that auto-renders URLS.

Source code::

    #!/bin/bash
    set -e
    set -u
    pandoc -f gfm -t docx $1 -o ${1%.md}.docx


md-to-pdf
------------------------------------------------------------------------

Use pandoc to convert a .md file to pdf.

I originally used the `markdown` format, but I've switched to `gfm`, github
flavoured markdown, because that auto-renders URLS.

Source code::

    #!/bin/bash
    set -e
    set -u
    pandoc -f gfm -t pdf $1 -o ${1%.md}.pdf


pychecker.sh
------------------------------------------------------------------------

Runs both pyflakes and pep8 on the current directory or on a specific
file. Very handy for code quality checks.

Note that it excludes the "migrations" directory that exists in Django
projects where you use South for database migrations. Those south-generated
files aren't the best pep8/pyflakes citizens (nor do they need to be).

Tip: add this to your emacs configuration and hook it up to ctrl-c ctrl-w
(which normally runs pychecker, hence the name) in python-mode::

    '(py-pychecker-command "pychecker.sh")
    '(py-pychecker-command-args (quote ("")))
    '(python-check-command "pychecker.sh")

Source code::

    #!/bin/bash

    # pyflakes $1 | grep -v /migrations/
    # echo "## pyflakes above, pep8 below ##"
    # pep8 --repeat --exclude migrations $1

    set -e
    flake8 "$1"


svngrep
------------------------------------------------------------------------

Grep for a term in the current directory, but with some twists:

- Multiple terms are taken to be one big space-separated term.

- ``.git`` and ``.hg`` directories are ignored.

- Same with ``egg-info`` and ``*.pyc`` files.

- The search term is highlighted in the output.

TODO: ignore big files (like combined js files).

Source code::

    #!/bin/bash

    SEARCHFOR=`echo "$*" | sed "s/ \/dev\/null//g"`
    grep -rin "$SEARCHFOR" * | grep -v \\.git | grep -v \\.hg | grep -v egg-info | grep -v \\.pyc: | grep -v \\.po: | grep -v bundle\\.js | grep -i --color=auto "$SEARCHFOR"


syncweblog.sh
------------------------------------------------------------------------

Purely personal. rsyncs my local html files with my webserver :-)

Source code::

    #!/bin/bash

    rsync -av ~/zelf/reinout.vanrees.org/docs/build/html/ tweetwee.vanrees.org:/srv/reinout.vanrees.org/var/www
