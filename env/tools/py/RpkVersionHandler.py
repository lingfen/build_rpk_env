# -*- coding: utf-8 -*
__auther__ = 'lingfen'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import json

class  VersionHandler:
    def __init__(self, jsonFile):
        self.jsonFile=jsonFile
        self.jsonfData={}
        self.load()

    def load(self):
        with open(self.jsonFile, 'r') as fp:
            self.jsonData = json.load(fp)

    def isPassableVersionName(self, versionName):
        if re.match("^\d+\.\d+\.\d+$", versionName):
            return True
        else:
            return False

    def setVersionName(self,versionName): 
        self.jsonData['versionName']=versionName


    def setVersionCode(self, versionCode):
        self.jsonData['versionCode']=versionCode

    def setIncVersionCode(self):
        versionCode = self.jsonData.get('versionCode')
        versionCode = str(int(versionCode) + 1)
        self.setVersionCode(versionCode)

    def cmpVersion(self, versionName):
        orgVersionName = self.jsonData.get('versionName')
        orgVersionNameList = re.split('\.', orgVersionName)
        versionNameList = re.split('\.', versionName)

        if len(orgVersionNameList) != len(versionNameList):
            #org veriosn not rule. so set versionName
            return 1

        for i in range(len(orgVersionNameList)):
            if int(orgVersionNameList[i]) < int(versionNameList[i]):
                return 1
            elif int(orgVersionNameList[i]) > int(versionNameList[i]):
                return -1
        return 1

    def dump(self):
        with open(self.jsonFile, 'w') as fp:
            json.dump(self.jsonData, fp,ensure_ascii=False, indent=0, separators=(',', ': '))
