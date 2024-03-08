"""
Create a directory and pre-fill it with an ``__init__.py``

Basically: mkdir plus the creation of the init file. Handy for creating a
django app's ``$APP/management/commands/`` directory.
"""

import os
import sys


def main():
    dirname = sys.argv[1]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print("Created directory %s" % dirname)
    initfile = os.path.join(dirname, "__init__.py")
    if not os.path.exists(initfile):
        open(initfile, "w").write("# package\n")
        print("Created file %s" % initfile)
