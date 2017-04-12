#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import os, sys, yaml, urllib2


def bitbar ():

    request = urllib2.urlopen('http://jutge.org/monitor')
    text = request.read()
    info = yaml.load(text)

    title = '♨ ' + info['queue'].replace(' ', '·')
    if info['zombies']:
    	title += ' 👻 %s' % info['zombies']


    loadavg = ' '.join(info['loadavg'].split()[:3])

    color = ' | color=black '

    print title, '| color=%s' % ('black' if info['queue_open'] else 'red')
    print '---'
    print 'Jutge.org | href=https://jutge.org', color
    print '---'
    print 'Queue is %s' % ('open | color=green' if info['queue_open'] else 'closed | color=red')
    print '---'
    print 'Subs and awards: %s %s' % (info['submissions_day'], info['awards_day']), color
    print 'Users: %s %s %s' % (info['users_day'], info['users_week'], info['users_month']), color
    print 'Disk usage: %s %s %s' % (info['avail_home'], info['avail_extra'], info['avail_tmp']), color
    print 'Loadavg: %s' % (loadavg, ), color




try:
    bitbar()
except:
    print '💣 Jutge'
