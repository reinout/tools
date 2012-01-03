"""
Script for running the jshint.js javascript checker on a file or directory.
"""
import commands
import os
import sys

import pkg_resources


JARFILE = pkg_resources.resource_filename('tools', 'rhino.jar')
RHINO = 'java -jar %s' % JARFILE
JSHINT = pkg_resources.resource_filename('tools', 'jshint.js')


def main():
    if not len(sys.argv) > 1:
        print "Usage: jshint script1.js [script2.js...]"
        print "   or: jshint directory"
        sys.exit(1)

    javascript_files = sys.argv[1:]
    if len(javascript_files) == 1:
        possible_dir = javascript_files[0]
        if os.path.isdir(possible_dir):
            javascript_files = []
            for (dirpath, dirnames, filenames) in os.walk(possible_dir):
                javascript_files += [
                    os.path.join(dirpath, filename) for filename in filenames
                    if filename.endswith('.js')]

    for javascript_file in javascript_files:

        (status, output) = commands.getstatusoutput(
            ' '.join([RHINO, JSHINT, javascript_file]))
        if status == 0:
            # Success!
            print "%s is OK" % javascript_file
        else:
            print "Error checking %s" % javascript_file
            print "exit code:", status
            print output
            sys.exit(status)
    sys.exit(0)
