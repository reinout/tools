"""Zap 'coding: utf-8' header from python files in the current directory.

The header isn't needed anymore in python 3, so for most projects, it can be
removed.

"""
from pathlib import Path


TO_REMOVE = "# -*- coding: utf-8 -*-"


def main():
    p = Path(".")
    for python_file in p.glob("**/*.py"):
        contents = python_file.read_text()
        if contents.startswith(TO_REMOVE):
            new_contents = contents.lstrip(TO_REMOVE).lstrip("\n")
            python_file.write_text(new_contents)
            print("Zapped coding header from %s" % python_file)
