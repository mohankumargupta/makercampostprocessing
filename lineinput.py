#! python3
import os
import fileinput
import re
import sys

filename = 'part.nc'
searchforfirstM3 = re.compile(r'M3')
flag = False
with fileinput.input(filename, inplace=True) as f:
  for line in f:
    if flag is False:
      match = searchforfirstM3.match(line)
      if match is not None:
  	    print('S255')
  	    flag = True
    print(line, end='')
