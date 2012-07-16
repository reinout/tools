"""
Open github page for your current directory in your browser.

You're working on the commandline and want to check something for the github
project you're working on. This script (called ``gh``) looks up the github url
for your project and opens it in your webbrowser.

If you call it like ``gh issues``, you'll get the issues page.

I got the idea from https://github.com/myusuf3/octogit.

"""
import commands
import re
import sys
import webbrowser

URL = 'https://github.com/{user}/{project}'
ISSUES_URL = 'https://github.com/{user}/{project}/issues'


def find_git_url(url_template):
    # A remotes line looks like this:
    # origin	git@github.com:reinout/tools.git (fetch)
    pattern = r"git@github.com:([^/]+)/(.+)\.git"
    regex = re.compile(pattern)
    output = commands.getoutput('git remote -v')
    for line in output.split('\n'):
        matches = regex.search(line)
        if matches:
            user, project = matches.groups()
            return url_template.format(user=user, project=project)


def main():
    if 'issues' in sys.argv:
        url_template = ISSUES_URL
    else:
        url_template = URL
    url = find_git_url(url_template=url_template)
    webbrowser.open(url)
