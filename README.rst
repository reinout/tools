Tools and scripts directory
===========================

I (`Reinout van Rees <http://reinout.vanrees.org>`_) use quite a number of
shell scripts, small custom Python utilities, other Python programs and so
on. In this project, I collect most of them.

The idea is that this directory's bin subdirectory is on my path.

- Shell scripts are located in ``shell/``. Running
  ``./install_shell_scripts.sh`` symlinks these into the ``bin/`` directory.

- The ``setup.py`` lists dependencies, such as pep8, pyflakes and
  zest.releaser.  Buildout installs those.

- The ``setup.py`` also has a couple of scripts of its own, in the ``tools/``
  directory.  These are also installed by buildout.


Useful to others? Yes, as examples and for copy-pasting of handy scripts
------------------------------------------------------------------------

The code in here can be useful to others: ideas for shell scripts and small
Python utilities. The ``svngrep`` shell script has found its way to several
colleague's computers, for instance.

So putting it on github seems like a good idea.


Bootstrap installation notes for myself
---------------------------------------

- Do a git pull of ``ssh://vanrees.org/~/git/Dotfiles`` into my homedir and
  run ``dotfiles --sync``: this gives me my dotfiles, including the
  checkoutmanager configuration. I need this because there are local
  development items I need to run.

- Symlink ``osx.cfg`` (on osx) or ``django.cfg`` (in my django vagrant box) to
  ``buildout.cfg`` first.

- Run ``/usr/bin/python2.7 bootstrap.py -t``. The ``-t`` is needed until
  buildout 2 is final.

- Run ``bin/buildout``


Extra OSX install notes
-----------------------

Install `homebrew <http://mxcl.github.com/homebrew/>`_ and install a couple of
utilities that are missing from OSX (or that are too old)::

    $ brew install wget gpg bash-completion svn htop siege

And, for the `git annex <http://git-annex.branchable.com/>`_ dependencies,
install::

    $ brew install haskell-platform git ossp-uuid md5sha1sum coreutils pcre


Documentation
-------------

I'm trying to do this the neat way: I've even added explanatory comments to
all shell scripts. And I've got a ``generate_shell_docs.py`` that generates a
README from those comments. Look in the shell directory (for instance `on
github <https://github.com/reinout/tools/tree/master/shell>`_) and you'll see
the nicely formatted README at the bottom.

Likewise I've got a README for the python scripts. Look `on github
<https://github.com/reinout/tools/tree/master/tools>`_ and you'll see the
nicely formatted README at the bottom. This is generated from the scripts'
docstrings with ``generate_python_docs.py`` (I just want a simple README, not
full Sphinx documentation).
