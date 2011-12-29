
Shell script documentation
==========================

Note: this documentation is automatically generated from the comments in the
shell scripts.



bzrdiff
------------------------------------------------------------------------

Show local differences in a bzr repository. In a bit nicer way than the bzr
default.

Source code::

    #!/bin/bash
    
    if [[ $* ]]; then
    WHERE=$*;
    else
    WHERE=".";
    fi
    bzr diff $WHERE | colordiff | less -R



dos2unix.py
------------------------------------------------------------------------



Source code::

    #!/usr/bin/env python
    
    # Copied from somewhere, I don't know wherefrom anymore.
    # What it does is convert from \r\n to just \n in case you've got files with
    # windows lineendings.
    
    # TODO: clean up a bit, make it pep8-compliant. Check that it works (as I had
    # the impression it didn't work all the time).
    
    from string import split,join
    def dos2unix(data):
    return join(split(data,'\r\n'),'\n')
    
    def unix2dos(data):
    return join(split(dos2unix(data),'\n'),'\r\n')
    def confirm(file):
    s=raw_input('%s? ' %file)
    return s and s[0]=='y'
    def usage():
    import sys
    print """\
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
    sys.exit()
    
    def main():
    import sys,re,os,shutil,getopt
    try:
    opts,args=getopt.getopt(sys.argv[1:],"fniuvdc")
    args[0]
    except:
    usage()
    force=0
    noaction=0
    convert=dos2unix
    verbose=0
    copystat=shutil.copymode
    backup='.bak'
    nobackup=0
    interactive=0
    for k,v in opts:
    if k=='-f':
    force=1
    elif k=='-n':
    noaction=1
    verbose=1
    elif k=='-i':
    interactive=1
    elif k=='-u':
    convert=unix2dos
    elif k=='-v':
    verbose=1
    elif k=='-b':
    backup=v
    elif k=='-d':
    copystat=shutil.copystat
    elif k=='-c':
    nobackup=1
    asciiregex=re.compile('[ -~\r\n\t\f]+')
    for file in args:
    if not os.path.isfile(file) or file[-len(backup):]==backup:
    continue
    fp=open(file)
    head=fp.read(10000)
    if force or len(head)==asciiregex.match(head):
    data=head+fp.read()
    #newdata=unix2dos(data)
    newdata=convert(data)
    if newdata!=data:
    if verbose and not interactive:
    print file
    if not interactive or confirm(file):
    if not noaction:
    newfile=file+'.@'
    f=open(newfile,'w')
    f.write(newdata)
    f.close()
    copystat(file,newfile)
    if backup:
    backfile=file+backup
    os.rename(file,backfile)
    else:
    os.unlink(file)
    os.rename(newfile,file)
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

Source code::

    #!/bin/bash
    
    # -h = Human readable
    # -c = Show the grand total, too.
    # -s = Show only the total size of the arguments: don't display the recursive
    #      information.
    
    du -hcs *



editexternals
------------------------------------------------------------------------

Shortcut for editing svn's externals property.

Source code::

    #!/bin/bash
    
    svn propedit svn:externals .



editignores
------------------------------------------------------------------------

Shortcut for editing svn's ignore property.

Source code::

    #!/bin/bash
    
    svn propedit svn:ignore .



es
------------------------------------------------------------------------

Shortcut for starting emacs on OSX.
Note that I've got it set up in server mode. I've got a bash alias "e" that
edits a file with "emacsclient". So "es" stands for "emacs server" in my
case, "e" is for editing with emacs itself :-)

Source code::

    #!/bin/bash
    
    /Applications/Emacs.app/Contents/MacOS/Emacs &



filefind
------------------------------------------------------------------------

Find filenames in the current directory:

- It greps case-insensitive for patial matches, so 'htm' finds 'index.HTML'
  just fine.
- It ignores .svn and .hg directories.
- It doesn't color code the output to help with emacs integration.
- It adds :1: so that you can use it in emacs' grep viewer. Clicking on it
  opens that file.

Source code::

    #!/bin/bash
    
    clear
    find -L . | grep --colour=never -i $1 | grep -v '.svn/' |grep -v '.hg/' |sed 's/^\.\///g'|sed 's/\(.*\)/\1:1:/g'
    # grep -i --color=auto $1



headdiff
------------------------------------------------------------------------

Show the changes made since our last "svn up" to trunk on the server.
Very handy if you suspect someone changed a lot and you want to review
whatever it is that an "svn up" is going to dump on your plate.

Source code::

    #!/bin/bash
    
    svn diff -rBASE:HEAD|colordiff|less



hgdiff
------------------------------------------------------------------------

Show colorized "hg diff" output for the current directory or for specific
files.

Source code::

    #!/bin/bash
    
    if [[ $* ]]; then
    WHERE=$*;
    else WHERE=".";
    fi
    hg diff -g $WHERE | colordiff | less -R



hglog
------------------------------------------------------------------------

Handy way to look at "hg log" without having to pipe it through "less"
ourselves. It uses the "-v" verbose flag, too.

Source code::

    #!/bin/bash
    
    hg -v log | less



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
    
    pyflakes $1 | grep -v /migrations/
    echo "## pyflakes above, pep8 below ##"
    pep8 --repeat --exclude migrations $1



svndiff
------------------------------------------------------------------------

Show "svn diff", but colorized and piped through "less".

Source code::

    #!/bin/bash
    
    if [[ $* ]]; then
    WHERE=$*;
    else
    WHERE=".";
    fi
    svn diff $WHERE | colordiff | less -R



svngrep
------------------------------------------------------------------------

Grep for a term in the current directory, but with some twists:

- Multiple terms are taken to be one big space-separated term.
- .svn and .hg directories are ignored.
- Same with egg-info and *.pyc files.
- The search term is highlighted in the output.

Source code::

    #!/bin/bash
    
    SEARCHFOR=`echo "$*" | sed "s/ \/dev\/null//g"`
    grep -rin "$SEARCHFOR" * | grep -v \\.svn | grep -v \\.hg | grep -v egg-info | grep -v \\.pyc | grep -i --color=auto "$SEARCHFOR"



syncweblog.sh
------------------------------------------------------------------------

Purely personal. rsyncs my local html files with my webserver :-)

Source code::

    #!/bin/bash
    
    rsync -av /Users/reinout/buildout/reinout.vanrees.org/docs/build/html/ vanrees.org:buildout/reinout.vanrees.org/docs/build/html



vlog
------------------------------------------------------------------------

Shows svn log, but with some better defaults:

- It uses verbose mode ("-v"); this way it actually shows the files that
  have been changed. This is often clearer than the log message itself.
- It pipes it through "less" instead of blubbering your terminal full with
  several pages' worth of logs.

Source code::

    #!/bin/bash
    
    svn -v log | less

