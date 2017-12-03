 #! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

BEFORE_TEXT = 1
MONTH_DATE = 2
DAY_DATE = 4
YEAR_DATE = 6
AFTER_TEXT = 8
# Create Regex that matches all file names for American MM-DD-YYYY format.
dateRegex = re.compile(r"""
	^(.*) # get rid of all text before date
	((0|1)\d)- # one or two digits for month
	((0|1|2|3)?\d)- # one or two digits day
	((19|20)\d\d) # year
	(.*?)$ # text after date
	""", re.VERBOSE)

# Loop over the files in the working directory.
for folderName, subfolders, filenames in os.walk(os.getcwd()):
	for filename in filenames:
		date = dateRegex.search(filename)
		if date == None:
			print("NONE YO")
		else:
			# gets all the different parts of the file.
			beforeText = date.groups(BEFORE_TEXT)
			monthDate = date.groups(MONTH_DATE)
			dayDate = date.groups(DAY_DATE)
			yearDate = date.groups(YEAR_DATE)
			afterText = date.groups(AFTER_TEXT)



# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.