"""
Simple script to add notes to a logfile from the command line.

The idea, that I read somewhere, is that a good engineer should keep logs of
what he does so that he can look at it later. It helps me quite a lot as I
regularly encounter a weird problem, knowing that I solved it earlier. But not
remembering what the solution was.

So either I have to write a blog entry about it so that I can find it in
google, or I need to add it to a simple text-based logfile somewhere. That's
what this script does.

"""
import logging
import os


LOGFILE = "~/engineer.log"
# ^^^ This one should be symlinked into some version controlled directory.
SEPARATOR = '\n-----'

logger = logging.getLogger('engineer')


def grab_input():
    """Grab and return input until the first empty line"""
    lines = []
    while 1:
        line = raw_input()
        # TODO: readline module gebruiken.
        if not line.strip():
            break
        lines.append(line)
    return lines


def main():
    logfile = os.path.expanduser(LOGFILE)
    logging.basicConfig(level=logging.INFO,
                        filename=logfile,
                        format="%(asctime)s %(message)s")
    entry = '\n'.join(grab_input())
    if not entry:
        return
    entry += SEPARATOR
    logging.info(entry)
