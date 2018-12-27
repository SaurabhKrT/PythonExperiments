

'''This program renames the PDF files in a folder with format 
"12344445-Some meaningful name.pdf" to "Some meaningful name.pdf"'''

import os

try:
  for file in os.listdir('folder path'):# lists the files in a given folder
    if(file.endswith('.pdf') and file[:1] in '0123456789'):# checks if the file has .pdf and start with numbers
      if file!=[]:# skips all empty lists
        parts = file.split('-')# split the the name into a list if - encountered
        if len(parts)>1:#checks if there are at least two elements in the list
          new_name = '{}'.format(parts[1])# using the 2nd element of the list create a new name
          src = 'folder path'+file
          dst  = 'folder path'+new_name
          os.rename(src, dst)
except:
  print("No such directory")

