from datetime import datetime
import os
import shutil
import subprocess
import sys
import webbrowser


DOCS = os.path.expanduser('~/buildout/reinout.vanrees.org/docs')
BUILD = os.path.join(DOCS, 'build', 'html')
WEBLOGSOURCE = os.path.join(DOCS, 'source', 'weblog')


def conditional_copy(source, target):
    if os.path.exists(target):
        old = open(target, 'r').read()
    else:
        old = None
    new = open(source, 'r').read()
    if new != old:
        open(target, 'w').write(new)
        print '.',


def copytoblog():
    """Copy text file to current date's blog dir"""
    if len(sys.argv) < 2:
        print "pass along filename!"
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print filename, "doesn't exist"

    now = datetime.now()
    y = '%04d' % now.year
    m = '%02d' % now.month
    d = '%02d' % now.day
    yeardir = os.path.join(WEBLOGSOURCE, y)
    monthdir = os.path.join(yeardir, m)
    daydir = os.path.join(monthdir, d)
    toplevel_added_dir = None
    add_index_dirs = []
    # mkdir
    for directory in [yeardir, monthdir, daydir]:
        if not os.path.exists(directory):
            os.mkdir(directory)
            add_index_dirs.append(directory)
            if toplevel_added_dir is None:
                toplevel_added_dir = directory

    # copy file
    target = os.path.join(daydir, filename)
    shutil.copyfile(filename, target)
    # touch missing index files
    for directory in add_index_dirs:
        index = os.path.join(directory, 'index.txt')
        open(index, 'w').write('temporary file\n')
    # svn add toplevel-dir-that-we-added
    if toplevel_added_dir:
        subprocess.call(['svn', 'add', toplevel_added_dir])
    else:
        subprocess.call(['svn', 'add', target])
    makedocs()
    html_file = target.replace('source', 'build/html').replace(
        '.txt', '.html')
    webbrowser.open(html_file)
    if 'y' in raw_input('Sync and commit? [y/N] '):
        subprocess.call(['syncweblog.sh'])
        os.chdir('/Users/reinout/buildout/reinout.vanrees.org'
                 '/docs/source/weblog')
        subprocess.call(['svn', 'commit', '-m', 'new entry'])
        on_site = 'http://reinout.vanrees.org/weblog/%s/%s/%s/%s' % (
            y, m, d, filename.replace('.txt', '.html'))
        webbrowser.open(on_site)
        if 'y' in raw_input('Delete file in ~/blog/? [y/N] '):
            os.remove(os.path.join('/Users/reinout/blog', filename))
            print "%s removed" % filename


def makedocs():
    """Call 'make html' in rvo's docs dir"""
    os.chdir(DOCS)
    subprocess.call(['make', 'html'])
    print "Syncing copyover dir"
    copydir = os.path.join(DOCS, 'copyover')
    for dirpath, dirnames, filenames in os.walk(copydir):
        if '.svn' in dirpath:
            continue
        targetdir = dirpath.replace('copyover', 'build/html')
        if not os.path.exists(targetdir):
            os.mkdir(targetdir)
            print "Created dir", targetdir
        for filename in filenames:
            if filename in ['.DS_Store']:
                continue
            if '~' in filename:
                continue
            source = os.path.join(dirpath, filename)
            target = source.replace('copyover', 'build/html')
            conditional_copy(source, target)


def list_todays_entries():
    now = datetime.now()
    y = '%04d' % now.year
    m = '%02d' % now.month
    d = '%02d' % now.day
    yeardir = os.path.join(WEBLOGSOURCE, y)
    monthdir = os.path.join(yeardir, m)
    daydir = os.path.join(monthdir, d)
    if not os.path.exists(daydir):
        print "Nothing posted yet in %s" % daydir
        sys.exit(1)
    entries = [entry for entry in os.listdir(daydir)
               if entry.endswith('.txt') and
               not entry == 'index.txt']
    entries = [os.path.join(daydir, entry) for entry in entries]
    subprocess.call(['emacs']
                    + entries)
