CONFIG_FILE = ('/Users/reinout/.thunderbird/fid7e99v.default/' +
               'News/newsrc-news.gmane.org')


def fix_thunderbird():
    """Fix the thunderbird newsrc settings

    The settings sometimes contain lines like::

      gmane.comp.python.distutils.devel: 1-12428,12431-12446

    There's a two-article 'hole' in there that shows up as two unread
    messages.  This script removes the holes.

    """

    lines = [line.strip() for line in open(CONFIG_FILE).readlines()]
    print "======= OLD ======="
    for line in lines:
        print line
    print "======= NEW ======="
    outfile = open(CONFIG_FILE, 'w')
    for line in lines:
        if not line:
            continue
        newsgroup, messages = line.split(': ')
        parts = messages.split('-')
        new = '%s: %s-%s\n' % (newsgroup,
                             parts[0],
                             parts[-1])
        print new,
        outfile.write(new)
    outfile.close()
