#!/usr/bin/env python
"""Generate a readme for the shell scripts."""
import os

OMIT = ['README.rst',
        ]
README_HEADER = """
Shell script documentation
==========================

Note: this documentation is automatically generated from the comments in the
shell scripts.

"""
SCRIPT_TEMPLATE = """

{script}
------------------------------------------------------------------------

{documentation}

Source code::

{code}

"""


def extract(script):
    """Return extracted code and documentation from script.

    Note that the code is indented four spaces to make it fit in the
    restructured text documentation.

    """
    lines = [line.rstrip() for line in open(script).readlines()]
    first_line = lines.pop(0)
    code_lines = [first_line]
    doc_lines = []
    in_doc_part = True
    for line in lines:
        if in_doc_part:
            if line.startswith('#'):
                doc_lines.append(line[2:])
                continue
            else:
                in_doc_part = False
        code_lines.append(line)

    doc = '\n'.join(doc_lines)
    code_lines = ['    ' + line for line in code_lines]
    code = '\n'.join(code_lines)
    return code, doc


def main():
    """Find the shell files and collect their inline documentation."""
    readme = README_HEADER
    os.chdir('shell')
    scripts = [script for script in os.listdir('.')
               if script not in OMIT]
    for script in scripts:
        code, documentation = extract(script)
        readme += SCRIPT_TEMPLATE.format(script=script,
                                         code=code,
                                         documentation=documentation)
    open('README.rst', 'w').write(readme)
    print "Wrote shell/README.rst"


if __name__ == '__main__':
    main()
