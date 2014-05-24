"""
Purpose: To snag which residues need to be converted to DNA from RNA

Syntax: python R2Dparser.py ~/Location/outputFileName 
    *Replace Location with location of the output file from charmm that lists the residues needing to be converted

Output: a file named patch.out with the patch expressions for in xrange(1,10):
  pass atoms from RNA to DNA

Note: The outputFileName from charmm must be 

Written by: Connor Fourt
Last Updated: May 23 2014
Written: May 23 2014
"""

from __future__ import print_function
from sys import argv 
import re


#taking in arguments and assigning them to i
i = argv
#making filenames
inputFileName = i[1]
outputFileName = "patch.out"


#priming files
f = open(inputFileName, 'r')
g = open(outputFileName, 'w')
f.seek(0) #Reset to beginning of file


#setting variables
patchesFound = 0
previousPatchFound = 0
lineNumber =0 
segid = raw_input("What is the segid? (should be defined at the top of your charmm input file)> " )
segid = segid + ' '
if len(segid) == 0: 
  segid = "segid "


#programatic sugar
print ('\nReading:', inputFileName)
print ('Writing to: ', outputFileName + '\n')

#console output
print('COPY BELOW THIS LINE'+ '\n')
print('-'*50 + '\n')

#finding patches and writing them to a file
for line in f:
  lineNumber = lineNumber + 1
  match = re.search(r'\d+\s+(\d+)\s+(\w\w\w)', line)
  numberMatch = re.search(r'9999',line)
  if match and numberMatch and match.group(1) and not previousPatchFound == match.group(1) :
    #updating the patch found variable so that no duplicates are found for a single residue
    previousPatchFound = match.group(1)
    atomNumber = match.group(1)
    residue = match.group(2)
    #if the residue has a cystine or thymine base, use pyrimadine patch
    if match.group(2) == "CYT" or match.group(2) == "THY":
      lineToWrite = ("patch deo1 " + str(segid) + str(match.group(1)) + '\n')
      g.write(lineToWrite)
      print (lineToWrite.rstrip('\n'))
      patchesFound = patchesFound + 1
    #if the residue has a guanine or adenine residue, use purine patch  
    elif match.group(2) == "GUA" or match.group(2) == "ADE":
      lineToWrite = ("patch deo2 " + str(segid) + str(match.group(1))+ '\n')
      g.write(lineToWrite)
      print (lineToWrite.rstrip('\n'))
      patchesFound = patchesFound + 1
   
print ()

#Prepending header and directions to patch.out
g.close()
g = open(outputFileName, 'r')
temp = g.read()
g.close()
g = open(outputFileName, 'w')
g.write(str(patchesFound) + ' patches found from ' + inputFileName + '\n'*2)
g.write('! deo1 is for pyrimidines' + '\n')
g.write('! deo2 is for purines' + '\n'*2)
g.write('COPY BELOW THIS LINE'+ '\n')
g.write('-'*50 + '\n'*2)
g.write(temp)

print ('Finished finding ' + str(patchesFound) + ' patches.')
print ('This can also be found in the file "patch.out" \n')
