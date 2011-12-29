#!/bin/bash
# Purely personal. rsyncs my local html files with my webserver :-)

rsync -av /Users/reinout/buildout/reinout.vanrees.org/docs/build/html/ vanrees.org:buildout/reinout.vanrees.org/docs/build/html
