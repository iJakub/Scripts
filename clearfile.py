#import
import sys
import os

#input
filepath = input("Enter path to file: ")
replace = input("Enter character to clear: ")

#script
with open(filepath) as fp:
    line = fp.readline()
    while line:
        for r in line:
            line = line.replace(replace, "")
        print(line, end='')
        line = fp.readline()
