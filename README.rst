Tools and scripts directory
===========================

I (`Reinout van Rees <https://reinout.vanrees.org>`_) use quite a number of
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

On **linux**, first some apt-get::

  sudo apt install python3-pip build-essential python3-venv git curl \
  make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
  libncursesw5-dev xz-utils tk-dev

on **OSX**, install `homebrew <https://brew.sh/>`_ and install a couple of
utilities that are missing from OSX::

  brew install git python@3.9

Then create an ssh key and arrange access to vanrees.org and github.com.

Checkout ourselves::

  mkdir -p ~/zelf
  cd ~/zelf
  git clone git@github.com:reinout/tools.git

Now install pipx, tools and dotfiles and checkouts and local dev installs::

  cd ~/zelf/tools
  make linux  # or make osx!

Note: I installed flake8 also with "pip install flake8" because that helps
emacs' flycheck to pick it up.


Extra linux install notes
-------------------------

And, as documentation, some of the ubuntu packages I install::

  apt install etckeeper gpg xclip emacs25 gnome-tweaks

For nextcloud, I `used the PPA
<https://launchpad.net/~nextcloud-devs/+archive/ubuntu/client>`_.


Extra OSX install notes
-----------------------

Programs to install:

- 1password

- iterm2

- synology drive client  


Documentation generation
------------------------

I'm trying to do this the neat way: I've even added explanatory comments to
all shell scripts. And I've got a ``generate_shell_docs.py`` that generates a
README from those comments. Look in the shell directory (for instance `;ppl at
shell on github <https://github.com/reinout/tools/tree/master/shell>`_) and
you'll see the nicely formatted README at the bottom.

Likewise I've got a README for the python scripts. Look `at /tools on github
<https://github.com/reinout/tools/tree/master/tools>`_ and you'll see the
nicely formatted README at the bottom. This is generated from the scripts'
docstrings with ``generate_python_docs.py`` (I just want a simple README, not
full Sphinx documentation).
