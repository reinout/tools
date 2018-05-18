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

- I use the `gp.recipe.node <https://pypi.python.org/pypi/gp.recipe.node>`_
  recipe to install some node/npm packages like jshint and lessc. Node is
  compiled locally and the scripts are installed simply into the ``bin/``
  directory with the rest.


Useful to others? Yes, as examples and for copy-pasting of handy scripts
------------------------------------------------------------------------

The code in here can be useful to others: ideas for shell scripts and small
Python utilities. The ``svngrep`` shell script has found its way to several
colleagues' computers, for instance.

So putting it on github seems like a good idea.


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


Installation on a VM TODO: update for ansible/vmware
----------------------------------------------------

I want most of my bash settings and helper scripts also in ubuntu VMs. I use
vmware fusion (and I used to use virtualbox+vagrant). I have a fabfile to do
the bootstrapping in there.

Prerequisites for vmware:

- I must be able to ssh into the machine, so "openssh-server" must be
  installed. This was missing from the two ubuntu server ISOs that I used, so
  that's something I need to do by hand.

- My home dir must be mounted on ``/mnt/hgfs/reinout``. Simply add my homedir
  in the "share" menu of the vmware config.

  The vmware tools must be installed for this. On ubuntu server images this
  might fail initially as the ``build-essential`` package isn't installed.
  After installing that, run ``vmware-config-tools.pl -d`` to get your vmware
  tools build with the defaults.

- Problem: files on that share are owned by ``501:dialout``, so modify the
  ``vmware_mount_vmhgfs`` function in ``/etc/vmware-tools/services.sh`` and
  add ``-o uid=1000,gid=1000`` to the mount command.


To install the tools and the dotfiles on the VM to prepare it so that I can
develop on it with pleasure, run::

    $ bin/fab -H VM_HOSTNAME vmware_bootstrap


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
