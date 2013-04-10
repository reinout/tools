#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import json
import urllib2
import sys
import re

if sys.platform.startswith('win'):
	GREEN = '{}'
	RED = '{}'
else:
	GREEN = '\x1b[1m\x1b[32m{}\x1b(B\x1b[m'
	RED = '\x1b[1m\x1b[31m{}\x1b(B\x1b[m'

TEMPLATE = '{NAAM:<35}{INTERN:>9}{MOBIEL:>13}  {PRESENCE:<20}'

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
print(63 * '-')

for elem in data[:-1]:
    if elem['in_office']:
        presence = GREEN.format('wel')
    else:
        presence = RED.format('niet')
    elem.update(PRESENCE=presence)
    text = TEMPLATE.format(**elem)
    if re.search(pattern, text, flags=re.IGNORECASE):
        print(text)
