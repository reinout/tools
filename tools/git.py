"""
Add/commit/push a git checkout in one command ("gac", for "Git Add Commit").

Lots of my personal stuff is in git, so I need to do a lot of ``git add -u``,
``git commit -m "update"`` and ``git push``. Note the ``"update"``
message. I'm often not bothering with more descriptive commit messages.

The script *does* ask for confirmation after first showing the status:
prevent accidents.

"""
import commands
import sys


def main():
    output = commands.getoutput('git status')
    print(output)
    if "Untracked files" in output:
        print('\n\n\n')
        print("Untracked files; do a manual 'git add -A'.")
        sys.exit(1)
    raw_input("Hit enter to continue add/commit/push cycle, ctrl-c to quit. ")
    print(commands.getoutput('git add -u'))
    print(commands.getoutput('git commit -m "Update"'))
    print(commands.getoutput('git push'))
