import webbrowser
import os

#script for opening chrome tabs
#these are the urls I want to open for work
urls = ['']
#for loop that opens each tab
for url in urls:
    webbrowser.open(url, new=2)

# script for opening discord
command = r'""' #add file path to desired app here
os.startfile(command)
