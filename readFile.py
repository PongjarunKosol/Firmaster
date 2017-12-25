#!/usr/bin/env python3
import os
import sys
import subprocess

class ReadFile:

	def __init__(self):
		self.file = "/home/firmaster/Desktop/result.txt"
		self.sharp = "#####"
		self.path_dict = {}
		self.topic = ""
		
	def printfile(self):
		with open(self.file, "r") as f: 
			for self.line in f: 
				self.selectLine(self.line)
			print self.path_dict

	def selectLine(self, line):
		
		cut = line[:5]

		if str(cut) == self.sharp:
			self.topic = line.split("#####################################")[1].rstrip().lstrip()
			self.path_dict.setdefault(self.topic, [])	
		else:
			if cut[0] == 'd':
				self.path_dict.setdefault(self.topic, []).append(line.replace("d","path",1))

	def print_dict(self):
		for key, value in self.path_dict.items():
			print("key: {} \t value: {}".format(key,value))

	def search_ssh(self):
		ssh_value = self.path_dict['ssh']
		if ssh_value:
			print("STATUS:     SSH value found!")
		else:
			print("STATUS:     No SSH value\n")

	def searching(self,key):
		value = self.path_dict[key]
		if value:
			print("STATUS:     "+ key +" value found!\n")
			print(self.path_dict[key])
		else:
			print("STATUS:     No "+ key +" value\n")		


if __name__ == "__main__": 
	
	#indentify what we want to check hear!!
	interest = ["passwd","shadow","ssh","ssl"]	

	print("---------- BINWALK ---------- \n")

	binwalk = subprocess.check_output(['binwalk','-e', '/home/firmaster/tools/fat/kkeps.bin'])

	print("EXTRACTED FILE SUCCESS\n")

	os.chdir('/home/firmaster/tools/firmwalker')

	print("---------- FIRMWALKER ----------\n")

	print("FINDING SSH . . .\n")

	result = subprocess.check_output(['/home/firmaster/tools/firmwalker/firmwalker.sh', '/home/firmaster/tools/firmwalker/_kkeps.bin.extracted','/home/firmaster/Desktop/result.txt'])
	
	with open("/home/firmaster/Desktop/result.txt", "a") as f:
		f.write(result)
	
	obj = ReadFile()

	obj.printfile()

	obj.search_ssh()
	

	for i in range(len(interest)):
	    obj.searching(interest[i])
	#obj.print_dict()	
	
