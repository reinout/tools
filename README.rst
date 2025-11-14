Tools and scripts directory
===========================

.. image:: https://results.pre-commit.ci/badge/github/reinout/tools/master.svg
   :target: https://results.pre-commit.ci/latest/github/reinout/tools/master
   :alt: pre-commit.ci status

I (`Reinout van Rees <https://reinout.vanrees.org>`_) use quite a number of shell
scripts, small custom Python utilities, other Python programs and so on. In this
project, I collect most of them.

The idea is that this directory's bin subdirectory is on my path.

- Shell scripts are located in ``shell/``. Running
  ``./install_shell_scripts.sh`` symlinks these into the ``bin/`` directory.

- The ``pyproject.toml`` lists the python scripts, in the ``tools/`` directory.
  These are installed with ``uv`` by the ``Makefile``.

And.... it is a way for me to be more **explicit** about my setup. A ``Makefile`` for
installing what I need (with homebrew and pipx) instead of trying to remember everything
I need whenever I move laptops. And some notes on how I set up my laptop in the first
place.


Useful to others? Yes, as examples and for copy-pasting of handy scripts
------------------------------------------------------------------------

The code in here can be useful to others: ideas for shell scripts and small Python
utilities. So putting it on github seems like a good idea. I've sometimes pointed
colleagues at a small utility here in this repo.


Bootstrap installation notes for myself (mac)
--------------------------------------------------------

These are the installations for really bootstrapping without anything present.

On my mac, install `homebrew <https://brew.sh/>`_ and install a couple of utilities that
are missing from OSX::

  brew install git python@3.13

Then create an ssh key and arrange access to vanrees.org and github.com.

Checkout ourselves::

  mkdir -p ~/zelf
  cd ~/zelf
  git clone git@github.com:reinout/tools.git

Now install uv, tools and dotfiles and checkouts and local dev installs::

  cd ~/zelf/tools
  make install

Note: the makefile also functions as a documentation on what I brew-install and
uv-tools-install.


Extra OSX install notes
-----------------------

Programs to install:

- 1password

- iterm2

- synology drive client

- tunnelblick

- docker desktop

Via app store:

- pixelmator pro

- BetterSnapTool


Documentation generation
------------------------

I'm trying to do this the neat way: I've even added explanatory comments to all shell
scripts. And I've got a ``generate_shell_docs.py`` that generates a README from those
comments. Look in the shell directory (for instance `;ppl at shell on github
<https://github.com/reinout/tools/tree/master/shell>`_) and you'll see the nicely
formatted README at the bottom.

Likewise I've got a README for the python scripts. Look `at /tools on github
<https://github.com/reinout/tools/tree/master/tools>`_ and you'll see the nicely
formatted README at the bottom. This is generated from the scripts' docstrings with
``generate_python_docs.py`` (I just want a simple README, not full Sphinx
documentation).


Local dev install notes
-----------------------

Some hints::

  $ uv sync
  $ uv run dtname (or another command)


Fresh laptop (2025) extra notes
-------------------------------

Settings:

- Dock: right + auto-hide.

- Modifier keys: caps=control, control=command, option=option, command=option.

- Display corners: top left "switch off screensaver".
