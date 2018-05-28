Tools and scripts directory
===========================

I (`Reinout van Rees <http://reinout.vanrees.org>`_) use quite a number of
shell scripts, small custom Python utilities, other Python programs and so
on. In this project, I collect most of them.

The idea is that this directory's bin subdirectory is on my path.

- Shell scripts are located in ``shell/``. Running
  ``./install_shell_scripts.sh`` symlinks these into the ``bin/`` directory.

- The ``setup.py`` lists the python scripts, in the ``tools/`` directory.
  These are installed with pipenv.


Useful to others? Yes, as examples and for copy-pasting of handy scripts
------------------------------------------------------------------------

The code in here can be useful to others: ideas for shell scripts and small
Python utilities. The ``svngrep`` shell script has found its way to several
colleagues' computers, for instance.

So putting it on github seems like a good idea.


Bootstrap installation notes for myself, to use on linux
--------------------------------------------------------

These are the installations for really bootstrapping without anything present.

- ``apt install python3-pip build-essential virtualenv``

- ``pip3 install pyenv``

- ``pyenv install 3.6.5`` and the same for 2.7.15

- Install pipsi: ``curl
  https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py |
  python``

With pipsi, you can then install various packages nicely isolated in their own
virtualenvs. First install "dotfiles" and "checkoutmanager" as we need them to
set up the rest.

- Do a git pull of ``ssh://vanrees.org/~/repos/Dotfiles`` into my homedir
  and run ``dotfiles --sync``: this gives me my dotfiles, including the
  checkoutmanager configuration. I need this because there are local
  development items I need to run.

- Symlink the desired checkoutmanager config in the homedir (``ln -s
  .checkoutmanager_linux.cfg .checkoutmanager.cfg``).

- Run ``checkoutmanager co``.

Now you can install this repo itself with a quick ``make install`` in
``~/zelf/tools``. It installs itself with pipsi.


Use pipsi to install a bunch of packages::

  pipsi install flake8
  pipsi install cookiecutter
  pipsi install docutils
  pipsi install isort
  pipsi install legit
  pipsi install oplop
  pipsi install ansible

And, as documentation, some of the debian packages I install::

  apt install etckeeper curl gpg xclip emacs25 evolution evolution-ews


Bootstrap installation notes for myself, to use on OSX
------------------------------------------------------

I work on a mac. So these are the installations for really bootstrapping
without anything present.

- Create a temporary virtualenv somewhere and install ``dotfiles`` and
  ``checkoutmanager`` in it.

- Do a git pull of ``ssh://vanrees.org/~/repos/Dotfiles`` into my homedir
  and run ``dotfiles --sync``: this gives me my dotfiles, including the
  checkoutmanager configuration. I need this because there are local
  development items I need to run. There's a bit of a bootstrap problem that
  ``dotfiles`` is actually installed by this tools dir :-)

- Symlink ``osx.cfg`` (on osx) to buildout.cfg`` first. The other ``.cfg`` are
  used inside virtualbox/vmware machines or on my own webserver.

- Run ``/usr/bin/python2.7 bootstrap.py`` and ``bin/buildout``.


Extra OSX install notes
-----------------------

Install `homebrew <http://mxcl.github.com/homebrew/>`_ and install a couple of
utilities that are missing from OSX (or that are too old)::

    $ brew install wget gpg bash-completion svn htop siege python

And, for the `git annex <http://git-annex.branchable.com/>`_ dependencies,
install::

    $ brew install haskell-platform git ossp-uuid md5sha1sum coreutils pcre


Documentation generation
------------------------

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
