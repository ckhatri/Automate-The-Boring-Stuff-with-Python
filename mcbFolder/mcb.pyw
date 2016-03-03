#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

LOAD_SAVE_LENGTH = 3
LOAD_KEY_POS = 2
LIST_LENGTH_COMMAND = 2
USER_COMMAND_POS = 1
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content.
if (len(sys.argv) == LOAD_SAVE_LENGTH):
	if (sys.argv[USER_COMMAND_POS].lower() == 'save'):
		mcbShelf[sys.argv[LOAD_KEY_POS]] = pyperclip.paste()
	elif (sys.argv[USER_COMMAND_POS].lower() == 'load'):
		keyword = sys.argv[LOAD_KEY_POS]
		keysVal = mcbShelf[keyword]
		if (keysVal != None):
			pyperclip.copy(str(keysVal))
		else:
			print("Could not find the keyword.")
# List keywords and load content.
elif (len(sys.argv) == LIST_LENGTH_COMMAND and sys.argv[USER_COMMAND_POS].lower() == 'list'):
	mcbKeys = mcbShelf.keys()
	print("List of keys saved:")
	for key in mcbKeys:
		print(key)

mcbShelf.close()