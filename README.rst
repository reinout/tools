Tools and scripts directory
===========================

I (`Reinout van Rees <http://reinout.vanrees.org>`_) use quite a number of
shell scripts, small custom Python utilities, other Python programs and so
on. In this project, I collect most of them.

The idea is that this directory's bin subdirectory is on my path.

- Shell scripts go in ``shell/``. Running ``./install_shell_scripts.sh``
  symlinks these into the ``bin/`` directory.

- The ``setup.py`` lists dependencies, such as pep8, pyflakes and
  zest.releaser. ``pip install .`` installs them all.

- The ``setup.py`` also has a couple of scripts of its own, in the ``tools/``
  directory. ``pip install .`` also installs those.


Useful to others? Yes, as examples and for copy-pasting of handy scripts
------------------------------------------------------------------------

The code in here can be useful to others: ideas for shell scripts and small
Python utilities. The ``svngrep`` shell script has found its way to several
colleague's computers, for instance.

So putting it on github seems like a good idea.


Two extra installation notes
----------------------------

- ``./install_local_checkouts.sh`` runs ``pip install`` on several checkouts
  of packages I develop myself, such as zest.releaser. So that I always run
  trunk to make sure everything works fine. Run this after everything is in
  place: we install checkoutmanager which we ourselves need as it does the
  checkouts we want to ``pip install`` :-)

- Run ``bin/pip install -r requirements.txt`` to make sure you end up with the
  right versions.


Documentation
-------------

I'm trying to do this the neat way: I've even added explanatory comments to
all shell scripts. And I've got a ``generate_shell_docs.py`` that generates a
README from those comments. Look in the shell directory (for instance `on
github <https://github.com/reinout/tools/tree/master/shell>`_) and you'll see
the nicely formatted README at the bottom.
