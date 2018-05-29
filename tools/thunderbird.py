"""Fix the thunderbird newsrc settings

The settings sometimes contain lines like::

  gmane.comp.python.distutils.devel: 1-12428,12431-12446

There's a two-article 'hole' in there that shows up as two unread messages.
This script removes the holes.

"""

CONFIG_FILE = ('/Users/reinout/Library/Thunderbird/Profiles/' +
               'rbwhgkue.default/News/newsrc-news.gmane.org')


def fix_thunderbird():
    """Remove holes in the config file."""

    lines = [line.strip() for line in open(CONFIG_FILE).readlines()]
    print("======= OLD =======")
    for line in lines:
        print(line)
    print("======= NEW =======")
    outfile = open(CONFIG_FILE, 'w')
    for line in lines:
        if not line:
            continue
        newsgroup, messages = line.split(': ')
        messages = messages.replace('-', ' ').replace(',', ' ')
        parts = messages.split()
        # new = '%s: %s-%s\n' % (newsgroup,
        #                        parts[0],
        #                        parts[-1])
        new = '%s: 1-%s\n' % (newsgroup,
                              parts[-1])
        print new,
        outfile.write(new)
    outfile.close()
