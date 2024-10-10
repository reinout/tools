
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
        s = input(f"{file_}? ")
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


    def main():  # noqa: C901
        try:
            opts, args = getopt.getopt(sys.argv[1:], "fniuvdc")
            args[0]
        except:  # noqa: E722
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


git-undelete
------------------------------------------------------------------------

Undelete a file from git which has been git-rm'ed and git-commit'ed somewhere in the
past. See https://stackoverflow.com/a/1113140/27401

Pass a filename (some_dir/some_file.txt) you want restored.

Source code::

    #!/bin/bash

    git checkout $(git rev-list -n 1 HEAD -- "$1")^ -- "$1"


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
    pandoc -f gfm+smart -t pdf $1 -o ${1%.md}.pdf


projectile-beautiful
------------------------------------------------------------------------

Run code beautification from emacs' projectile

I often want to run `black` or `ruff format` and so on the code for
basic code beautification. This script is coupled to `C-c b` in
emacs, it is intended to work inside a projectile project.

- If the environment variable `PROJECTILE_BEAUTIFUL` is set, run that
  command. The direnv program can help you set it automatically.

- If a makefile is present, `make beautiful` is run.

- `ruff format` is run


Source code::

    #!/bin/bash

    set -e
    if [ -n "$PROJECTILE_BEAUTIFUL" ]; then
        eval $PROJECTILE_BEAUTIFUL
        exit
    fi

    if [ -f Makefile ]; then
        exec make beautiful
    fi

    exec ruff format .


projectile-check
------------------------------------------------------------------------

Run code checks from emacs' projectile

I often want to run `pyflakes` or `ruff check` and so on the code
for basic structure and syntax checking. This script is coupled to
C-c c` in emacs, it is intended to work inside a projectile project.

- If the environment variable `PROJECTILE_CHECK` is set, run that
  command. The direnv program can help you set it automatically.

- If a makefile is present, `make check` is run.

- `ruff` is run with check+fix as a fallback.


Source code::

    #!/bin/bash

    set -e
    if [ -n "$PROJECTILE_CHECK" ]; then
        eval $PROJECTILE_CHECK
        exit
    fi

    if [ -f Makefile ]; then
        exec make check
    fi

    exec ruff check . --fix


projectile-test
------------------------------------------------------------------------

Run tests from emacs' projectile

Emacs' projectile project tool can run tests with `C-c p P`. I have
that coupled to `C-c t`. In one project, you need to run
`bin/pytest`, in another `make test`, in another
`venv/bin/pytest`... This script attempts a couple of them. Note
that projectile runs it in the project's root directory: handy.

- If the environment variable `PROJECTILE_TEST` is set, run that
  command. The direnv program can help you set it automatically.

- If a makefile is present, `make test` is run.

- bin/pytest (and the venv/.venv variants) is searched for and run
  if found.

Source code::

    #!/bin/bash

    set -e
    if [ -n "$PROJECTILE_TEST" ]; then
        eval $PROJECTILE_TEST
        exit
    fi

    if [ -f Makefile ]; then
        exec make test
    fi

    for program in bin/pytest venv/bin/pytest .venv/bin/pytest
    do
        if [ -f $program ]; then
            exec $program
        fi
    done

    echo "No test program found"
    exit 1


syncweblog.sh
------------------------------------------------------------------------

Purely personal. rsyncs my local html files with my webserver :-)

Source code::

    #!/bin/bash

    rsync -av ~/zelf/reinout.vanrees.org/docs/build/html/ tweetwee.vanrees.org:/srv/reinout.vanrees.org/var/www
