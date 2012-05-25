#!/bin/bash
# Initialize a git repository in the temp directory and push it to my own
# server. I should have created a repository there on the server already with
# ``git init ~/git/the_project_name --bare``.

cd /tmp
git init $1
cd $1
echo "hurray" > README.rst
git add README.rst
git commit -m "Added readme"
git remote add origin ssh://vanrees.org/~/git/$1
git push origin master
