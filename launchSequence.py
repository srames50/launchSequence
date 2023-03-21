import webbrowser
import subprocess
import os

# Script for opening Chrome tabs
# These are the URLs I want to open for work
urls = [
    '',
    '',
    '',
    ''
]

# For loop that opens each tab
for url in urls:
    webbrowser.open(url, new=2)

# Script for opening Discord
command = [''] #add file path here
subprocess.Popen(command)