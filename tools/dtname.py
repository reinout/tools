"""
Helper script to generate a zettelkasten ID (YYYYMMDDHHMM-some-info.md) filename

dtname by itself just outputs ``202208171545.md``, ``dtname some info`` gives
you ``202208171545-some-info.md``

"""

import datetime
import re
import sys
import unicodedata


INBOX = "~/syn/notes/0-inbox/"


def slugify(value):
    # Copied from https://github.com/django/django/blob/main/django/utils/text.py
    value = str(value)
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s\-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def main():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    words = sys.argv[1:]
    if words:
        text = " ".join(words)
        filename = timestamp + "-" + slugify(text) + ".md"
    else:
        filename = timestamp + ".md"

    print()
    print(len(INBOX) * " " + filename)
    print(INBOX + filename)
    print()


if __name__ == "__main__":
    main()
