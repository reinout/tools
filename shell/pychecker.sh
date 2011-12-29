#!/bin/bash
pyflakes $1 | grep -v /migrations/
echo "## pyflakes above, pep8 below ##"
pep8 --repeat --exclude migrations $1
