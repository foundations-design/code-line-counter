#!/usr/bin/env python

# This Python script counts the lines of code in the directory in which it is
# run.  It only looks at files which end in the file extensions passed to the
# script as arguments.

# It outputs counts for total lines, blank lines, comment lines and code lines
# (total lines minus blank lines and comment lines).

# Example usage and output:
# > lines_of_code_counter.py .h .cpp
# Total lines:   15378
# Blank lines:   2945
# Comment lines: 1770
# Code lines:    10663

# TODO:
# - Accept "dir" as argument
# - Move to `/scratchpad/lines-of-code`
# - Create README.md
#     - include snippet to get lines of code in 1) BDI Quote Tool and 2) eMTF

# Change this value based on the comment symbol used in your programming
# language.
commentSymbol = "//"

import sys
import os, os.path

acceptableFileExtensions = sys.argv[1:]
if not acceptableFileExtensions:
   print("Please pass at least one file extension as an argument.")
   quit()

currentDir = os.getcwd()

filesToCheck = []
for root, _, files in os.walk(currentDir):
   for f in files:
      fullpath = os.path.join(root, f)
      if ".git" not in fullpath:
         for extension in acceptableFileExtensions:
            if fullpath.endswith(extension):
               filesToCheck.append(fullpath)

if not filesToCheck:
   print("No files found.")
   quit()

lineCount = 0
totalBlankLineCount = 0
totalCommentLineCount = 0

print("")
print("lines\tblank lines\tcomment lines\tcode lines\t\tFilename")

for fileToCheck in filesToCheck:
   with open(fileToCheck, encoding="utf8") as f:

      fileLineCount = 0
      fileBlankLineCount = 0
      fileCommentLineCount = 0

      for line in f:
         lineCount += 1
         fileLineCount += 1

         lineWithoutWhitespace = line.strip()
         if not lineWithoutWhitespace:
            totalBlankLineCount += 1
            fileBlankLineCount += 1
         elif lineWithoutWhitespace.startswith(commentSymbol):
            totalCommentLineCount += 1
            fileCommentLineCount += 1

      print(
          format(fileLineCount) + "\t" + format(fileBlankLineCount) + "\t\t" +
          format(fileCommentLineCount) + "\t\t" +
          format(fileLineCount - fileBlankLineCount - fileCommentLineCount) +
          "\t\t" + format(os.path.basename(fileToCheck)))

#

print("")
print("Totals")
print("--------------------")
print("Lines:         " + format(lineCount))
print("Blank lines:   " + format(totalBlankLineCount))
print("Comment lines: " + format(totalCommentLineCount))
print("Code lines:    " +
      format(lineCount - totalBlankLineCount - totalCommentLineCount))
