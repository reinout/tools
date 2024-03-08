"""
Helper scripts for me to manage my blog.

I write my blog entries as restructured text files. The ``copytoblog`` command
copies the text file to the correct date's blog subdirectory, creating it if
necessary.

There's also a command to open today's entries in emacs.

Note that some of this might be better placed inside my website project
instead of here. TODO.

"""

from datetime import datetime
from string import Template
import os
import readline
import shutil
import subprocess
import sys
import webbrowser

DOCS = os.path.expanduser("~/zelf/reinout.vanrees.org/docs")
BUILD = os.path.join(DOCS, "build", "html")
WEBSITECONTENT = os.path.expanduser("~/zelf/websitecontent")
WEBLOGSOURCE = os.path.expanduser("~/zelf/websitecontent/source/weblog")
SERMONSOURCE = os.path.expanduser("~/zelf/websitecontent/source/preken")


def conditional_copy(source, target):
    if os.path.exists(target):
        old = open(target).read()
    else:
        old = None
    new = open(source).read()
    if new != old:
        open(target, "w").write(new)
        print(".")


def copytoblog():
    """Copy text file to current date's blog dir"""
    if len(sys.argv) < 2:
        print("pass along filename!")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("%s doesn't exist" % filename)

    now = datetime.now()
    y = "%04d" % now.year
    m = "%02d" % now.month
    d = "%02d" % now.day
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
        index = os.path.join(directory, "index.txt")
        open(index, "w").write("temporary file\n")
    # git add toplevel-dir-that-we-added
    os.chdir(WEBLOGSOURCE)
    if toplevel_added_dir:
        subprocess.call(["git", "add", toplevel_added_dir])
    else:
        subprocess.call(["git", "add", target])
    # Add all updated files.
    subprocess.call(["git", "add", "-u"])
    makedocs()
    html_file = (
        target.replace("source/", "docs/build/html/")
        .replace(".txt", ".html")
        .replace("websitecontent", "reinout.vanrees.org")
    )
    webbrowser.open("file://" + html_file)
    if "y" in input("Sync and commit? [y/N] "):
        subprocess.call(["syncweblog.sh"])
        os.chdir(WEBSITECONTENT)
        subprocess.call(["git", "commit", "-m", "new entry"])
        subprocess.call(["git", "push"])
        on_site = "https://reinout.vanrees.org/weblog/{}/{}/{}/{}".format(
            y,
            m,
            d,
            filename.replace(".txt", ".html"),
        )
        webbrowser.open(on_site)
        if "y" in input("Delete file in ~/blog/? [y/N] "):
            os.remove(os.path.join(os.path.expanduser("~/blog"), filename))
            print("%s removed" % filename)


def makedocs():
    """Call 'make html' in rvo's docs dir"""
    os.chdir(DOCS)
    subprocess.call(["make", "html"])
    # Not needed anymore: we do a simple "copy -r" in the makefile.
    # print "Syncing copyover dir"
    # copydir = os.path.join(DOCS, 'copyover')
    # for dirpath, dirnames, filenames in os.walk(copydir):
    #     if '.svn' in dirpath:
    #         continue
    #     targetdir = dirpath.replace('copyover', 'build/html')
    #     if not os.path.exists(targetdir):
    #         os.mkdir(targetdir)
    #         print "Created dir", targetdir
    #     for filename in filenames:
    #         if filename in ['.DS_Store']:
    #             continue
    #         if '~' in filename:
    #             continue
    #         source = os.path.join(dirpath, filename)
    #         target = source.replace('copyover', 'build/html')
    #         conditional_copy(source, target)


def list_todays_entries():
    """Open today's entries in emacs (to correct mistakes, probably)."""
    now = datetime.now()
    y = "%04d" % now.year
    m = "%02d" % now.month
    d = "%02d" % now.day
    yeardir = os.path.join(WEBLOGSOURCE, y)
    monthdir = os.path.join(yeardir, m)
    daydir = os.path.join(monthdir, d)
    if not os.path.exists(daydir):
        print("Nothing posted yet in %s" % daydir)
        sys.exit(1)
    entries = [
        entry
        for entry in os.listdir(daydir)
        if entry.endswith(".txt") and not entry == "index.txt"
    ]
    entries = [os.path.join(daydir, entry) for entry in entries]
    subprocess.call(["emacs"] + entries)


def _complete(text, state, tags):
    for tag in tags:
        if tag.startswith(text):
            # print("\n" + tag)
            if not state:
                return tag
            else:
                state -= 1


def complete_churches(text, state):
    churches_dir = os.path.join(SERMONSOURCE, "kerken")
    churches = [f[:-4] for f in os.listdir(churches_dir) if f.endswith(".txt")]
    return _complete(text, state, churches)


def complete_reverents(text, state):
    reverents_dir = os.path.join(SERMONSOURCE, "predikanten")
    reverents = [f[:-4] for f in os.listdir(reverents_dir) if f.endswith(".txt")]
    return _complete(text, state, reverents)


def new_sermon():
    """Create a new file for my sermon weblog."""
    now = datetime.now()
    added = "%04d-%02d-%02d" % (now.year, now.month, now.day)

    # http://stackoverflow.com/questions/7116038/python-tab-completion-mac-osx-10-7-lion
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

    date = None
    while not date:
        date = input("Datum (yyyy-mm-dd): ")
    yyyy = str(int(date[:4]))
    yeardir = os.path.join(SERMONSOURCE, yyyy)
    if not os.path.exists(yeardir):
        os.mkdir(yeardir)
        print("Created %s" % yeardir)

    title = None
    while not title:
        title = input("Titel: ")

    filename = (
        title.replace(" ", "-").replace(",", "").replace("'", "").lower()[:50] + ".txt"
    )
    full_filename = os.path.join(yeardir, filename)
    print(f"Using filename {full_filename}")

    readline.set_completer(complete_churches)
    church = None
    while not church:
        church = input("Kerk: ")

    readline.set_completer(complete_reverents)
    reverent = None
    while not reverent:
        reverent = input("Predikant: ")
    # ^^^ Refactor the while loops above.

    template = Template(
        """${title}
======================================================================

.. preek::
   :kerk: ${church}
   :toegevoegd: ${added}
   :datum: ${date}
   :predikant: ${reverent}
   :tekst: TODO
   :tags:

"""
    )
    output = template.substitute(
        title=title, church=church, added=added, date=date, reverent=reverent
    )
    open(full_filename, "w").write(output)
    print("Opening with emacs: " + full_filename)
    emacs = "/opt/homebrew/bin/emacsclient"
    # subprocess.call(['emacs', full_filename])
    os.execl(emacs, "-n", full_filename)
