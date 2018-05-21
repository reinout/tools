#!/bin/bash
# Purely personal. rsyncs my local html files with my webserver :-)

rsync -av /home/reinout/zelf/reinout.vanrees.org/docs/build/html/ vanrees.org:/srv/reinout.vanrees.org/var/www
