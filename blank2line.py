# coding=utf-8

import re
import os





#  single file process

with open ('segmented/all_files.txt') as f_in:
	contents = f_in.read()
	
# contents = re.sub("[A-Za-z\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", contents_raw)

# print contents
with open ('ResultFromAll_file.txt' , 'w') as f_out:
	f_out.write(contents.replace(' ','\n'))





'''
# delete strings but the result is bad (Garbled 乱码)
with open ('out1.txt') as f:
	trans_in = f.read()

trans_out = re.sub("[A-Za-z\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", trans_in)

with open ('out2.txt' , 'w') as f_trans:
	f_trans.write(trans_out)i
print trans_outi

'''
