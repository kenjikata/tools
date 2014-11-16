# -*- coding: utf-8 -*-
import codecs
import sys
import re

fin  = codecs.open(“aa.txt",'r',"utf-8")
fout = codecs.open(“bb.txt",'w',"utf-8")

def write(line):
	try:
		fout.write(line)
	except IOError,e:
		print (e.args[1])

def main():
	try:
		lines = fin.readlines()
		for line in lines:
			line = re.sub('　','',line) # 全角スペースを削る
			line = re.sub('https?://.*','',line) # URLを削る
			line = line.strip().split('\n')
			#write(line)
			print line

		fin.close()
		fout.close()

	except IOError,e:
		print (e.args[1])

if __name__ == '__main__':
	main()
