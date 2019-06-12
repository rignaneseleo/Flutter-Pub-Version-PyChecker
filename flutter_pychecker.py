#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tool to find the last version of Flutter plugins
# Credits Leonardo Rignanese <dev.rignaneseleo@gmail.com>
# Github: https://github.com/rignaneseleo

from six.moves import urllib
from pyquery import PyQuery as pq

startWord="#vcontrol-start"#the word where to start the scan
endWord="#vcontrol-end"#the word where to end the scan
indent="  "#the chars to intend the pubspec.yaml in the plugins part

#Intro
print("\n\n--Flutter Pub Version PyChecker--")
print("\nThis is a free open source tool to quikly get the list of the last versions of your Flutter plugins.\nYou will insert the path of your pubspec.yaml that MUST contain "+startWord+" before the first plugin and "+endWord+" after the last plugin you want to analyze.")

#Get the pubspec
print("Insert the absolute path of your pubspec.yaml: ")
pubspecPath=raw_input()
try:
    pubspec=open(pubspecPath,"r").read().strip()#read pubspec.yaml
except:
    print("Error. Can't find or open your pubspec.yaml")
    quit()

#Handle the pubspec
pubspecLines=pubspec.split("\n")#get every line of the file
pubspecLines=([x.strip() for x in pubspecLines])#strip the list
pubspecLines = filter(None, pubspecLines)#remove empty spaces

#Get the plugin list
try:
    startRow=pubspecLines.index(startWord)+1
    endRow=pubspecLines.index(endWord)
except:
    print("Error. Did you add "+startWord+" before the first plugin and "+endWord+" after the last plugin you want to analyze?")
    quit()

#Handle the plugin list
pluginListRaw=pubspecLines[startRow:endRow]#get the list of plugins
pluginList=[row for row in pluginListRaw if row[0]!="#"]#remove commented ones
print("\nFound "+str(len(pluginList))+" plugins:")

#Handle every plugin
updatedPluginList="\n"
for pluginNameRaw in pluginList:
    pluginName=pluginNameRaw.split()[0][:-1]#get the plugin name
    pluginVersion=pluginNameRaw.split()[1]#get the plugin version

    _url='https://pub.dev/packages/'+pluginName#create the url
    jquery=pq(url=_url)#load the url

    #check if the page is found
    if(jquery(".package-list").html()==None):
        lastVersion=jquery(".version-table > tbody > tr").attr("data-version")#get the version
        updatedPluginList+=indent+pluginName+": ^"+lastVersion+"\n"
        print("\tThe last version of " + pluginNameRaw+ " is " + lastVersion)#print version
    else:
        print("Unable to find the plugin page of "+pluginName)#print error


print("\nDo you want to see the list updated to copy and paste in your pubspec.yaml?[Y/n]")
answer=raw_input()
if(answer.lower()!="n"):

    #include also the commented
    commentedPluginListRaw=[indent+row for row in pluginListRaw if row[0]=="#"]#save commented ones
    commentedPluginList='\n'.join(commentedPluginListRaw)+"\n"

    print("\n"
        +startWord
        +updatedPluginList
        +commentedPluginList
        +endWord
        +"\n")

print("END")
print("\nCredits by Leonardo Rignanese <dev.rignaneseleo@gmail.com>\n\n\n")