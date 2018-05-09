# coding=utf-8

import re
import os

# the path of dir
filedir = os.getcwd() + '/data_raw'

# get the files in dir
filenames = os.listdir(filedir)

# open the output file
with open ('result.txt','a') as f_out:

	# read the files in dir
	for filename in filenames:
		filepath = filedir+'/'+filename
		with open (filepath) as f_in:
			contents = f_in.read()
		f_out.write(contents.replace(' ','\n'))




