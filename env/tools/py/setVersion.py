#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import getopt
import json
from RpkVersionHandler import *

class OPtions(object): pass
Options= OPtions()

def usage():
    print '-h,--help: print help message.'
    print '-v, --version: print script version'

def getOpt(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'hv:f:', ['help','jsonFile=', 'versionName='])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    
    for o, a in opts:
        #print o,a
        if o in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif o in ('-v', '--versionName'):
            Options.versionName = a.strip()
        elif o in ('-f', '--jsonFile'):
            Options.jsonFile = a
        else:
            print 'unhandled option'
            usage()
            sys.exit(3)

def main(argv):
    getOpt(argv)
    appVersionHandler = VersionHandler(Options.jsonFile)
    if not appVersionHandler.isPassableVersionName(Options.versionName):
        print '版本号格式不对，正确的应该是x.x.x,只能有3段,并且x为数字.'
        return -1
        
    if appVersionHandler.cmpVersion(Options.versionName) == -1 :
        print '配置的版本号小于当前版号'
        return -1
    else:
        appVersionHandler.setVersionName(Options.versionName)
        appVersionHandler.setIncVersionCode()
        appVersionHandler.dump()

if __name__ == '__main__':
    main(sys.argv)

