#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename, summary):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  #---------------2nabanana starts here---------------------#
  """
  f = open(filename, 'r')
  text = f.read()
  f.close()
  filename.close()
  """
  n=0
  dictname={}
  listyearname=[]
  input_file = open(filename, 'r')
  """if not inputfile:
    print( "There is no such file")
    return
  """
  for line in input_file:
    #print("line number",n)
    n=n+1
    if line.startswith('<h3'):
      print("line number",n)
      words = line.split('>')
      for word in words:
        print(word)
        if word.startswith('Popularity'):
          year = word[14:18]
          print("year and line", year, n)
          break
    #print("h3 found n",n )
    if line.startswith('<tr') and line.endswith('td>\n'):
    #if line.endswith('td>\n'):
      print("line",line)
      words = line.split('><td>')
      rank=words[1][0:-4]
      malename=words[2][0:-4]
      femalename=words[3][0:-6]
      print("rank, name1 name2", rank, malename, femalename)
      if malename not in dictname:
        dictname[malename]=rank
      if femalename not in dictname:
        dictname[femalename]=rank
  #print("dictname", sorted(dictname.items()))
  
  input_file.close() 
  

  #listyearname.append(year)
  #listyearname.append(sorted(dictname.items()))
  summaryfile= year+'_Name.summary'
  if not summary:
    print ("dictname\n", listyearname)
  else:
    filenana = open(summaryfile,'w')
    filenana.write(year)
    filenana.write('\n')
    words = sorted(dictname.keys())
    for word in words:
      filenana.write(word)
      filenana.write(' ')
      filenana.write(dictname[word])
      filenana.write('\n')
      
    filenana.close()
    
  #----------------2nabanana ends here----------------------#
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  #---------------2nabanana starts here---------------------#
  if not summary:
    extract_names(args[0], 0)
  else:
    extract_names(args[0], 1)
  #----------------2nabanana ends here----------------------#
  
if __name__ == '__main__':
  main()
