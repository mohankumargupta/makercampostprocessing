#! python3

#import sys
#print(sys.version)

from subprocess import call
from pathlib import Path
import os
import fileinput
import re
import sys


def findFilesInbox():
  p = Path('.\\inbox')
  return p

def insertS255(filename):
  searchforfirstM3 = re.compile(r'M3')
  flag = False
  with fileinput.input(filename, inplace=True) as f:
    print(filename)
    for line in f:
      if flag is False:
        match = searchforfirstM3.match(line)
        if match is not None:
          print('S255')
          flag = True
   
      print(line, end='')


files = findFilesInbox()
for file in files.iterdir():
  infile = 'inbox\\' + file.name
  outfile = 'converted\\' + file.name
  movedfile = 'outbox\\' + file.name
  if (os.path.isfile(movedfile)):
    os.remove(movedfile)
  call(['gcodelaseropt', infile ,'-o', outfile])
  os.rename(infile, movedfile)
  insertS255(outfile)




