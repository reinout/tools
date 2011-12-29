#!/bin/bash
# Runs both pyflakes and pep8 on the current directory or on a specific
# file. Very handy for code quality checks.
#
# Note that it excludes the "migrations" directory that exists in Django
# projects where you use South for database migrations. Those south-generated
# files aren't the best pep8/pyflakes citizens (nor do they need to be).
#
# Tip: add this to your emacs configuration and hook it up to ctrl-c ctrl-w
# (which normally runs pychecker, hence the name) in python-mode::
#
#     '(py-pychecker-command "pychecker.sh")
#     '(py-pychecker-command-args (quote ("")))
#     '(python-check-command "pychecker.sh")

pyflakes $1 | grep -v /migrations/
echo "## pyflakes above, pep8 below ##"
pep8 --repeat --exclude migrations $1
