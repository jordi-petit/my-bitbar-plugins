#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

if len(sys.argv) == 1:
#   print 'Ξ'
    print '💻'
    print '---'
    print 'Hide desktop icons | terminal=false bash=%s param1=hide' % sys.argv[0]
    print 'Show desktop icons | terminal=false bash=%s param1=show' % sys.argv[0]
elif sys.argv[1] == 'hide':
   os.system('defaults write com.apple.finder CreateDesktop false && killall Finder')  
elif sys.argv[1] == 'show':
   os.system('defaults write com.apple.finder CreateDesktop true  && killall Finder')     