# Data_Preprocessing

If you need combine all the files in a dictory to a file ,you can execute like this:
``` bash
find . -type f -exec cat {} \;>all_files.txt 
```
If you want to convert all blanks in a file into line breaks, you can execute:
``` python
python blank2line.py
```
If you want to convert all blanks in all files in a dictory into line breaks, you can execute:
``` python
python blankline.py
```
