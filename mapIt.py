#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
# example: mapIt 870 Valencia St, San Francisco, CA 94110

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address rom clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)