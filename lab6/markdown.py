"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertOne(line):
  line = re.sub(r'#(.*)', r'<h1>\1</h1>', line)
  return line

def convertTwo(line):
  line = re.sub(r'##(.*)', r'<h2>\1</h2>', line)
  return line

def convertThree(line):
  line = re.sub(r'###(.*)', r'<h3>\1</h3>', line)
  return line

def startBlock(line):
  line = re.sub(r'>(.*)', r'<blockquote>\1', line)
  usingBlock = True
  return line

def endBlock(line):
  line = '</blockquote>' + line
  usingBlock = False
  return line

def continueBlock(line):
  line = re.sub(r'>(.*)', r'\1', line)
  return line

def checkBlock(line):
  if(line[0] == '>'):
    return True
  else:
    return False

usingBlock = False

for line in fileinput.input():
  line = line.rstrip() 
  if (checkBlock(line)):
    #if it has a >
    if usingBlock == False:
      startBlock(line)
    elif usingBlock == True:
      continueBlock(line)
  elif (usingBlock == True):
    endBlock(line)


  line = convertStrong(line)
  line = convertEm(line)
  line = convertThree(line)
  line = convertTwo(line)
  line = convertOne(line)
  print '<p>' + line + '</p>',
