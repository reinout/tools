#!/bin/bash
# Purely personal. rsyncs my local html files with my webserver :-)

rsync -av /Users/reinout/git/reinout.vanrees.org/docs/build/html/ vanrees.org:buildout/reinout.vanrees.org/docs/build/html
rsync -av /Users/reinout/git/reinout.vanrees.org/docs/build/html/ new.vanrees.org:git/reinout.vanrees.org/docs/build/html
