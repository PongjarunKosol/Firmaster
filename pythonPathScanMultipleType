#!/usr/bin/python

import os
from subprocess import call
import sys
import csv

# traverse root directory, and list directories as dirs and files as files
#original = str(raw_input("PATH: "))
original = "/home/firmaster/Desktop/firmwares/_rootfs.squashfs.extracted/"
directory = original+"_copy"

TypeOfFiles = ["php","js","c","cpp","html"]
TagetDir = ["phpFile","jsFile","cFile","cppFile","htmlFile"]

call(["cp","-r",original,directory])
for i in range(5):
	for root, dirs, files in os.walk(directory):
	    path = root.split(os.sep)
	    #print((len(path) - 1) * '---', os.path.basename(root))
	    #for file in files:
		#print(len(path) * '---', file)
	    abspath = str(os.path.abspath(root))
	    #print("This is path: ",abspath)
	    call(["classifier","-st",TypeOfFiles[i],"-sf","/home/firmaster/Desktop/"+TagetDir[i],"-d",abspath])
    	    #call(["classifier","-st","php","-sf","/home/firmaster/Desktop/phpFile","-d",abspath])	

call(["rm","-r",directory])
