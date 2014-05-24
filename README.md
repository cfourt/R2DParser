R2DParser
=========

Charmm requires a patch to recognize that nitrogenous bases are deoxy versus oxy. This parser outputs the various residues that require a patch by identifying those atoms in nitrogenous bases that do not have a coordinate for their respective O2' oxygens. 

Syntax: python R2Dparser.py ~/Location/outputFileName 
    *Replace Location with location of the output file from charmm that lists the residues needing to be converted

Output: a file named patch.out with the patch expressions for in xrange(1,10):
  pass atoms from RNA to DNA

Note!!!: The outputFile from charmm must be contain the command coor print for
this script to read corretly.    

Written by: Connor Fourt
Last Updated: May 23 2014
Written: May 23 2014
