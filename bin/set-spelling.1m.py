#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
import sys


if len(sys.argv) == 1:

    cmd = 'defaults read "Apple Global Domain" NSPreferredSpellServerLanguage'
    what = commands.getstatusoutput(cmd)[1]

    langs = {
        'ca_ES': 'Català',
        'es_ES': 'Castellano',
        'en_US': 'English (US)',
    }

    print('📖')
    print('---')
    for code, text in langs.items():
        if code == what:
            text = "✓ " + text
        print('%s | refresh=true terminal=false bash=%s param1=%s' % (text, sys.argv[0], code))

else:

    os.system("defaults write 'Apple Global Domain' NSPreferredSpellServerLanguage %s" % sys.argv[1])
