'''This program renames the files in a folder with format 
12344445-Some meaningful name.pdf to Some meaningful name.pdf'''

import os
import re

try:
  for file in os.listdir('/home/saurabhtiwari/Desktop/Analytics Book/'):# lists the files in a given folder
    if(re.search('.pdf', file) and file[:1] in '0123456789'):# checks the files with .pdf text
      if file!=[]:# skips all empty lists
        parts = file.split('-')# split the the name into a list if - encountered
        if len(parts)>1:#checks if there are at least two elements in the list
          new_name = '{}'.format(parts[1])# using the 2nd part of list create a new name
          src = '/home/saurabhtiwari/Desktop/Analytics Book/'+file
          dst  = '/home/saurabhtiwari/Desktop/Analytics Book/'+new_name
          os.rename(src, dst)
except:
  print("No such directory")

