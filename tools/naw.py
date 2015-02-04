# -*- coding: utf-8 -*-
"""
Company-internal script to query our telephone list.

We have an internal tool that regularly pings laptops to see if somebody's in
the house. That data, combined with a telephone number list, is available as a
JSON file.

This script reads the json and prints it, optionally filtered with

(Script is from Arjan Verkerk, not me, btw. Though I modified it a bit to run
as a setuptools console script.)

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import re
import sys
import urllib2

GREEN = '\x1b[1m\x1b[32m{}\x1b(B\x1b[m'
RED = '\x1b[1m\x1b[31m{}\x1b(B\x1b[m'
TEMPLATE = '{NAAM:<35}{number:>9}{MOBIEL:>13}  {PRESENCE:<20}'


def main():
    jsonfile = urllib2.urlopen(
        'http://buildbot.lizardsystem.nl/gis/aanwezigheid.json',
    )
    data = json.load(jsonfile)
    jsonfile.close()

    try:
        pattern = sys.argv[1]
    except IndexError:
        pattern = ''

    print('   Gericht overnemen: *59 / Prefix interne nummers: 030 2330')
    print(TEMPLATE.format(NAAM='Naam',
                          number='Nummer',
                          MOBIEL='Mobiel',
                          PRESENCE='Aanwezig?'))

    print(68 * '-')

    for elem in data[:-1]:
        if not elem['in_office']:
            presence = RED.format('niet')
        elif elem['in_drieharingen']:
            presence = GREEN.format('3 Haringen')
        else:
            presence = GREEN.format('Zakkendrager')

        elem.update(PRESENCE=presence)
        text = TEMPLATE.format(**elem)
        if re.search(pattern, text, flags=re.IGNORECASE):
            print(text)
