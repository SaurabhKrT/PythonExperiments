'''8.16 Exercises
Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order.'''

lst = list() #Creates an empty list
fhand = open('/folder/romeo.txt')
for line in fhand:
  word = line.rstrip().split(' ') #Split the lines and new line characters
  for element in word: 
    if element not in lst: #For each element in word checks if element is not in the lst
      lst.append(element) #When found append new element to lst
      lst.sort() 
print lst

'''
Result: 

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 
'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 
'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 
'through', 'what', 'window', 'with', 'yonder']
'''
