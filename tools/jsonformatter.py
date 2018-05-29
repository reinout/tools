"""(Re-)indent json on stdin and send it to stdout.

Handy for webservices that return json as one big long string. With ``curl
http://the.json.url/ | jsonformatter`` you can actually read it.


"""
import json
import sys


def main():
    the_json = json.loads(sys.stdin.read())
    print(json.dumps(the_json, indent=4))
