#!bin/python
"""Generate a readme for the shell scripts."""
import os
import sys

OMIT = ['__init__.py',
        ]
BASE_GITHUB_URL = 'https://github.com/reinout/tools/blob/master/tools/'
README_HEADER = """
Python script documentation
===========================

Note: this documentation is automatically generated from the docstrings at the
top of the Python scripts.

"""
SCRIPT_TEMPLATE = """

{script}
------------------------------------------------------------------------

{documentation}

(See `source code on github <{github_url}>`_).

"""


def main():
    """Find the Python files and collect their inline documentation."""
    readme = README_HEADER
    os.chdir('tools')
    scripts = [script for script in os.listdir('.')
               if script.endswith('.py') and script not in OMIT]
    for script in scripts:
        module_name = 'tools.' + script[:-3]
        __import__(module_name)
        documentation = sys.modules[module_name].__doc__
        github_url = BASE_GITHUB_URL + script
        readme += SCRIPT_TEMPLATE.format(script=script,
                                         documentation=documentation,
                                         github_url= github_url)
    open('README.rst', 'w').write(readme)
    print "Wrote tools/README.rst"


if __name__ == '__main__':
    main()
