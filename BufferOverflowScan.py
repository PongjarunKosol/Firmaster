#!/usr/bin/python

import os
from subprocess import call
import sys
import csv

# traverse root directory, and list directories as dirs and files as files
#directory = str(raw_input("PATH: "))
directory = ["/home/firmaster/Desktop/cFile","/home/firmaster/Desktop/cppFile"]
for i in range(2):
    for root, dirs, files in os.walk(directory[i]):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)
        abspath = str(os.path.abspath(root))
        print("This is path: ",abspath)
        call(["rats","--column","--context",abspath])
