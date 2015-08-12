#! python3

#import sys
#print(sys.version)

from subprocess import call
from pathlib import Path
import os
import fileinput
import re
import sys
import tkinter 
import tkinter.filedialog 

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

file = tkinter.filedialog.askopenfilenames( )
if (file):
  originalfilefullpath = file[0]
  originalfilebasename = os.path.basename(originalfilefullpath)
  originalfiledirname = os.path.dirname(originalfilefullpath)
  originalfilename = originalfilebasename.split('.')[0]
  originalfilenameextension = originalfilebasename.split('.')[-1]
  outfile = originalfiledirname + '/' + originalfilename + "_laser." + originalfilenameextension
  infile = originalfilefullpath
  call(['gcodelaseropt', infile ,'-o', outfile])
  insertS255(outfile)

