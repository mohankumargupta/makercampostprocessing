#! python

#import sys
#print(sys.version)

from subprocess import call
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
  for line in fileinput.input(filename, inplace=True):
    if flag is False:
      match = searchforfirstM3.match(line)
      if match is not None:
        print('S255')
        flag = True
   
    print line,
  fileinput.close()


#files = findFilesInbox()
files = os.listdir('.\\inbox')
for filename in files:
  infile = 'inbox\\' + filename
  outfile = 'converted\\' + filename
  movedfile = 'outbox\\' + filename
  if (os.path.isfile(movedfile)):
    os.remove(movedfile)
  call(['gcodelaseropt', infile ,'-o', outfile])
  os.rename(infile, movedfile)
  insertS255(outfile)




